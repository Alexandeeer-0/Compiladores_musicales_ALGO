#le metemos sus imports IMPORTANTISIMO
import sys #esto para interactuar con el interprete y el sistema
from antlr4 import * #esto para interactuar con el lexer y el parser
from AlgoritmiaLexer import AlgoritmiaLexer #esto para interactuar con el lexer
from AlgoritmiaParser import AlgoritmiaParser #esto para interactuar con el parser
from AlgoritmiaInterpreter import AlgoritmiaVisitor #esto para interactuar con el visitante

#definimos la funcion main
def main():
    # Verificamos que se ha pasado un archivo como argumento
    if len(sys.argv) != 2:
        #sys.argv[0] es el nombre del script
        print("Usage: python algoritmia.py <source_file>")
        return

    try:
        # Abrimos el archivo de código fuente con codificación UTF-8
        input_stream = FileStream(sys.argv[1], encoding='utf8')
        #sys.argv[1] sera el archivo a procesar y FileStream es una clase de ANTLR que maneja la entrada del archivo

        # Creamos un Lexer y un Parser para el código fuente:
        lexer = AlgoritmiaLexer(input_stream)
        #El lexer divide el texto en tokens (unidades léxicas)
        stream = CommonTokenStream(lexer)
        #CommonTokenStream es una clase de ANTLR que maneja los tokens
        parser = AlgoritmiaParser(stream)
        #El parser analiza los tokens y construye el árbol de sintaxis


        # Parseamos el código y generamos el árbol de sintaxis
        tree = parser.root()

        # Creamos el visitante para recorrer el árbol y ejecutar el código
        visitor = AlgoritmiaVisitor()

        #visit(tree) recorre el árbol ejecutando las acciones correspondientes
        visitor.visit(tree)
        

        # Generamos los archivos de música midi y lilypond
        visitor.generate_midi()
        visitor.generate_lilypond()
        
    #si ocurre un error, lo atrapamos y mostramos el mensaje de error
    except Exception as e:
        print(f"Error: {str(e)}")
        return

#si el archivo se ejecuta directamente, se llama a la funcion main
if __name__ == '__main__':
    main()
