from AlgoritmiaParser import AlgoritmiaParser
from AlgoritmiaVisitor import AlgoritmiaVisitor as BaseVisitor
import operator
from collections import defaultdict
import os
import subprocess
import mido
from mido import MidiFile, MidiTrack, Message


# Environment for managing variables and notes
class AlgoritmiaEnv:
    def __init__(self):
        self.variables = {}
        self.notes = {
            "C": 60, "D": 62, "E": 64, "F": 65, "G": 67,
            "A": 69, "B": 71
        }

    def get(self, var):
        if var not in self.variables:
            print(f"Warning: Variable '{var}' not defined")
            return None
        return self.variables.get(var)

    def set(self, var, value):
        self.variables[var] = value


# Visitor class for interpreting the Algoritmia language
class AlgoritmiaVisitor(BaseVisitor):
    def __init__(self):
        super().__init__()
        self.procs = {}
        self.env = AlgoritmiaEnv()
        self.midi_notes = []
        self.lily_notes = []
        self.tempo = 120  # Default tempo (BPM)
        self.volume = 64  # Default volume (0-127)
        
        # Path to LilyPond executable
        self.lilypond_path = r"C:\Users\alxpe\PYCharm\lilypond-2.24.4\bin\lilypond.exe"

    def visitRoot(self, ctx):
        # Visit all procedure definitions first
        for proc in ctx.procDef():
            self.visit(proc)
        
        # Then call the main procedure if it exists
        if 'PlayMelody' in self.procs:
            self.call_proc('PlayMelody', [])
        return None

    def visitInss(self, ctx):
        result = None
        for ins in ctx.ins():
            result = self.visit(ins)
        return result

    def visitOutput_(self, ctx):
        for expr in ctx.expr():
            value = self.visit(expr)
            print(f"Output: {value}")
        return None

    def visitAssign(self, ctx):
        var_name = ctx.VAR().getText()
        value = self.visit(ctx.expr())
        self.env.set(var_name, value)
        return None

    def visitReprod(self, ctx):
        note = self.visit(ctx.expr())
        if isinstance(note, str):
            # Process for MIDI
            midi_note = self.env.notes.get(note, 60)
            self.midi_notes.append((midi_note, self.volume))
            
            # Process for LilyPond (convert to lowercase)
            lily_note = note.lower()
            self.lily_notes.append(lily_note)
            
            print(f"Playing note: {note}")
        return None

    def visitCondition(self, ctx):
        cond = self.visit(ctx.expr())
        if cond:
            return self.visit(ctx.inss(0))
        elif len(ctx.inss()) > 1:
            return self.visit(ctx.inss(1))
        return None

    def visitWhile_(self, ctx):
        while self.visit(ctx.expr()):
            self.visit(ctx.inss())
        return None

    def visitLista(self, ctx):
        return [self.visit(expr) for expr in ctx.expr()]

    def visitNota(self, ctx):
        return ctx.getText()

    def safe_operation(self, left, right, op):
        if left is None or right is None:
            return None
        try:
            return op(left, right)
        except (TypeError, ValueError) as e:
            print(f"Warning: Operation failed - {e}")
            return None

    def visitMul(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return self.safe_operation(left, right, operator.mul)

    def visitDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if right == 0:
            print("Warning: Division by zero")
            return None
        return self.safe_operation(left, right, operator.truediv)

    def visitMod(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if right == 0:
            print("Warning: Modulo by zero")
            return None
        return self.safe_operation(left, right, operator.mod)

    def visitSum(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if isinstance(left, list) and isinstance(right, list):
            return left + right
        return self.safe_operation(left, right, operator.add)

    def visitMin(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return self.safe_operation(left, right, operator.sub)

    def visitGt(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return self.safe_operation(left, right, operator.gt)

    def visitLt(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return self.safe_operation(left, right, operator.lt)

    def visitGet(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return self.safe_operation(left, right, operator.ge)

    def visitLet(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return self.safe_operation(left, right, operator.le)

    def visitEq(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return self.safe_operation(left, right, operator.eq)

    def visitNeq(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return self.safe_operation(left, right, operator.ne)

    def visitNum(self, ctx):
        try:
            return float(ctx.getText())
        except ValueError:
            print(f"Warning: Invalid number format - {ctx.getText()}")
            return None

    def visitVar(self, ctx):
        return self.env.get(ctx.getText())

    def visitString(self, ctx):
        text = ctx.getText()
        return text[1:-1]  # Remove quotes

    def visitSz(self, ctx):
        var_name = ctx.siz().VAR().getText()
        value = self.env.get(var_name)
        if isinstance(value, list):
            return len(value)
        return 0

    def visitConsul(self, ctx):
        var_name = ctx.consult().VAR().getText()
        index = int(self.visit(ctx.consult().expr()))
        value = self.env.get(var_name)
        if isinstance(value, list) and 0 <= index < len(value):
            return value[index]
        return None

    def visitProcDef(self, ctx):
        proc_name = ctx.PROCNAME().getText()
        params = [param.getText() for param in ctx.paramsId().VAR()]
        self.procs[proc_name] = {"params": params, "body": ctx.inss()}
        return None

    def visitProc(self, ctx):
        proc_name = ctx.PROCNAME().getText()
        if proc_name not in self.procs:
            print(f"Error: Procedure '{proc_name}' not defined")
            return None
        proc = self.procs[proc_name]
        param_values = [self.visit(expr) for expr in ctx.paramsExpr().expr()]
        return self.call_proc(proc_name, param_values)

    def call_proc(self, proc_name, param_values):
        proc = self.procs[proc_name]
        old_values = {}
        
        # Save old values and set new parameter values
        for param, value in zip(proc["params"], param_values):
            old_values[param] = self.env.get(param)
            self.env.set(param, value)
        
        # Execute procedure body
        result = self.visit(proc["body"])
        
        # Restore old values
        for param, value in old_values.items():
            if value is not None:
                self.env.set(param, value)
            else:
                self.env.variables.pop(param, None)
        
        return result

    def visitCorte(self, ctx):
        var_name = ctx.VAR().getText()
        index = int(self.visit(ctx.expr()))
        lista = self.env.get(var_name)
        if isinstance(lista, list) and 0 <= index < len(lista):
            value = lista.pop(index)
            return value
        return None

    def visitAgregado(self, ctx):
        var_name = ctx.VAR().getText()
        value = self.visit(ctx.expr())
        lista = self.env.get(var_name)
        if not isinstance(lista, list):
            lista = []
            self.env.set(var_name, lista)
        lista.append(value)
        return None

    def generate_midi(self):
        print("Generating MIDI file...")
        midi_file = MidiFile()
        track = MidiTrack()
        midi_file.tracks.append(track)

        # Add notes with volume
        for note, volume in self.midi_notes:
            track.append(Message('note_on', note=note, velocity=volume, time=0))
            track.append(Message('note_off', note=note, velocity=volume, time=500))

        midi_file.save('output.mid')
        print("MIDI file 'output.mid' has been generated.")

    def generate_lilypond(self):
        print("Generating LilyPond file...")
        lily_content = f"""\\version "2.24.0"
\\header {{
    title = "Simple Melody"
    composer = "Generated by Algoritmia"
    tagline = "Created with LilyPond"
}}

\\paper {{
    #(set-paper-size "a4")
    top-margin = 15
    left-margin = 15
    right-margin = 10
    bottom-margin = 15
}}

\\score {{
    \\relative c' {{
        \\tempo 4 = {self.tempo}
        \\time 4/4
        \\clef treble
        \\key c \\major
        
        {' '.join(note + '4 ' for note in self.lily_notes)}
        \\bar "|."
    }}
    \\layout {{ 
        indent = #0
    }}
    \\midi {{ }}
}}"""
        
        with open('output.ly', 'w', encoding='utf-8') as f:
            f.write(lily_content)
        print("LilyPond file 'output.ly' has been generated.")
        
        # Generate PDF using LilyPond
        print("Generating PDF score...")
        try:
            result = subprocess.run([self.lilypond_path, 'output.ly'], 
                                 capture_output=True, 
                                 text=True)
            if result.returncode == 0:
                print("PDF score has been generated successfully.")
            else:
                print(f"Error generating PDF: {result.stderr}")
        except Exception as e:
            print(f"Error running LilyPond: {str(e)}")

