import sys
from antlr4 import *
from AlgoritmiaLexer import AlgoritmiaLexer
from AlgoritmiaParser import AlgoritmiaParser
from AlgoritmiaInterpreter import AlgoritmiaVisitor

def main():
    # Verificamos que se ha pasado un archivo como argumento
    if len(sys.argv) != 2:
        print("Usage: python algoritmia.py <source_file>")
        return

    try:
        # Abrimos el archivo de código fuente con codificación UTF-8
        input_stream = FileStream(sys.argv[1], encoding='utf8')

        # Creamos un Lexer y un Parser para el código fuente
        lexer = AlgoritmiaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = AlgoritmiaParser(stream)

        # Parseamos el código y generamos el árbol de sintaxis
        tree = parser.root()

        # Creamos el visitante para recorrer el árbol y ejecutar el código
        visitor = AlgoritmiaVisitor()

        # Ejecutamos el visitante y obtenemos el resultado
        visitor.visit(tree)
        
        # Generamos los archivos de música
        visitor.generate_midi()
        visitor.generate_lilypond()
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return

if __name__ == '__main__':
    main()
