#le metemos sus imports tmb IMPORTANTISIMO
from AlgoritmiaParser import AlgoritmiaParser #esto para interactuar con el parser
from AlgoritmiaVisitor import AlgoritmiaVisitor as BaseVisitor #esto para interactuar con el visitante
import operator #esto para interactuar con los operadores
from collections import defaultdict #esto para interactuar con los diccionarios
import os #esto para interactuar con el sistema de archivos
import subprocess #esto para interactuar con el sistema de procesos
from mido import MidiFile, MidiTrack, Message #esto para interactuar con los archivos midi


#definimos la clase AlgoritmiaEnv para interactuar con el entorno de ejecución
class AlgoritmiaEnv:
    def __init__(self):
        self.variables = {} #diccionario para almacenar las variables
        self.notes = { #diccionario para almacenar las notas
            "C": 60, "D": 62, "E": 64, "F": 65, "G": 67,
            "A": 69, "B": 71
        } #ACA ESTAN LAS NOTAS PIANOS QUE DICE EN EL DOCUMENTO

    #definimos la funcion get para obtener el valor de una variable
    def get(self, var):
        if var not in self.variables:
            print(f"Warning: Variable '{var}' not defined")
            return None
        return self.variables.get(var)

    #definimos la funcion set para asignar un valor a una variable
    def set(self, var, value):
        self.variables[var] = value


#definimos la clase AlgoritmiaVisitor para interpretar el lenguaje Algoritmia
class AlgoritmiaVisitor(BaseVisitor):
    def __init__(self):
        super().__init__()
        self.procs = {} #diccionario para almacenar las procedimientos
        self.env = AlgoritmiaEnv() #instancia de la clase AlgoritmiaEnv
        self.midi_notes = [] #lista para almacenar las notas midi
        self.lily_notes = [] #lista para almacenar las notas lilypond
        self.tempo = 120  # Default tempo (BPM) esto es la velocidad de la musica EL TEMPOOOOOO WUU
        self.volume = 64  # Default volume (0-127) 
        
        #ruta del ejecutable de lilypond p mi chill de cojones
        self.lilypond_path = r"C:\Users\alxpe\Desarrollo-de-Compiladores-e-Interpretes-Notas-Musical\PROYECTO_ALGORITMIA\lilypond-2.24.2-mingw-x86_64.exe"

    #definimos la funcion visitRoot para visitar el nodo raiz del arbol de sintaxis
    def visitRoot(self, ctx):
        for proc in ctx.procDef():
            self.visit(proc)
        
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
            midi_note = self.env.notes.get(note, 60)
            self.midi_notes.append((midi_note, self.volume))
            
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
        return text[1:-1] 

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
        
        for param, value in zip(proc["params"], param_values):
            old_values[param] = self.env.get(param)
            self.env.set(param, value)
        
        result = self.visit(proc["body"])
        
        for param, value in old_values.items():
            if value is not None:
                self.env.set(param, value)
            else:
                self.env.variables.pop(param, None)
        
        return result

    #definimos la funcion visitCorte para visitar el nodo corte del arbol de sintaxis
    def visitCorte(self, ctx): #ctx es el contexto actual
        var_name = ctx.VAR().getText() #obtenemos el nombre de la variable
        index = int(self.visit(ctx.expr())) #obtenemos el indice de la lista
        lista = self.env.get(var_name) #obtenemos la lista de la variable
        if isinstance(lista, list) and 0 <= index < len(lista): #si la lista existe y el indice es valido
            value = lista.pop(index) #eliminamos el elemento de la lista
            return value #devolvemos el valor eliminado
        return None #si no hay lista o el indice no es valido, devolvemos None

    #definimos la funcion visitAgregado para visitar el nodo agregado del arbol de sintaxis
    def visitAgregado(self, ctx): 
        var_name = ctx.VAR().getText() 
        value = self.visit(ctx.expr()) 
        lista = self.env.get(var_name)
        if not isinstance(lista, list):
            lista = []
            self.env.set(var_name, lista)
        lista.append(value)
        return None

    #definimos la funcion generate_midi para generar el archivo midi
    def generate_midi(self):
        print("Generating MIDI file...")
        midi_file = MidiFile() #creamos un archivo midi
        track = MidiTrack() #creamos una pista midi
        midi_file.tracks.append(track) #agregamos la pista al archivo

        for note, volume in self.midi_notes:
            track.append(Message('note_on', note=note, velocity=volume, time=0)) #agregamos el mensaje de inicio de nota
            track.append(Message('note_off', note=note, velocity=volume, time=500)) #agregamos el mensaje de fin de nota

        midi_file.save('output.mid') #guardamos el archivo midi
        print("MIDI file 'output.mid' has been generated.")

    #definimos la funcion generate_lilypond para generar el archivo lilypond
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
        
        with open('output.ly', 'w', encoding='utf-8') as f: #abrimos el archivo lilypond
            f.write(lily_content) #escribimos el contenido del archivo lilypond
        print("LilyPond file 'output.ly' has been generated.")
        
        print("Generating PDF score...")
        try:
            result = subprocess.run([self.lilypond_path, 'output.ly'], #ejecutamos el comando de lilypond
                                 capture_output=True, #capturamos la salida
                                 text=True) #decodificamos la salida como texto
            if result.returncode == 0:
                print("PDF score has been generated successfully.")
            else:
                print(f"Error generating PDF: {result.stderr}")
        except Exception as e:
            print(f"Error running LilyPond: {str(e)}")

