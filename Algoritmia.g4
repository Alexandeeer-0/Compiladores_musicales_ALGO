grammar Algoritmia;

/* 
 * Gramática para un lenguaje de programación musical
 * Permite crear música mediante algoritmos
 * Incluye operaciones con listas y notas musicales
 *
 * Ejemplos de uso:
 * - Asignación:    variable <- 42
 * - Lista:         lista <- {1 2 3}
 * - Reproducir:    (:) C4
 * - Agregar:       lista << elemento
 * - Cortar:        8< lista[0]
 */

// Punto de entrada - Un programa es una secuencia de definiciones de procedimientos
root: procDef* EOF;

// Secuencia de instrucciones - Puede contener 0 o más instrucciones
inss: ins*;

// Tipos de instrucciones permitidas:
// - Estructuras de control (if, while)
// - Operaciones básicas (input, output, llamadas a procedimientos, asignaciones, reproducción)
// - Operaciones de lista (agregar, cortar)
ins: (condition | while_)
    | (input_ | output_ | proc | assign | reprod)
    | (agregado | corte) ;

// Entrada/Salida
input_: '<?>' VAR;      // Entrada: <?> variable
output_: '<w>' expr+;   // Salida: <w> expresión

// Estructuras de control
condition: 'if' expr LB inss RB ('else' LB inss RB)?;  // if condición |: instrucciones :| else |: instrucciones :|
while_: 'while' expr LB inss RB;                       // while condición |: instrucciones :|

// Operaciones musicales
reprod: REPROD expr;    // Reproducir nota: (:) C4
REPROD: '(:)';          // Símbolo de reproducción musical

// Operaciones con listas
agregado: VAR AGREGADO expr;        // Agregar elemento: lista << elemento
AGREGADO: '<<';                     // Operador de agregación

corte: CORTA VAR LS expr RS;        // Cortar elemento: 8< lista[índice]
CORTA: '8<';                        // Operador de corte

// Procedimientos
procDef: PROCNAME paramsId LB inss RB;    // Definición: PROC param1 param2 |: instrucciones :|
proc: PROCNAME paramsExpr (expr)*;         // Llamada: PROC arg1 arg2

// Asignaciones y parámetros
assign: VAR ASSIGN expr;    // variable <- expresión
ASSIGN: '<-';              // Operador de asignación
paramsId: (VAR)*;          // Lista de parámetros en definición
paramsExpr: (expr)*;       // Lista de argumentos en llamada

// Listas y acceso
lista : '{' expr* '}';              // Definición de lista: {1 2 3}
consult: VAR LS expr RS;            // Acceso a lista: lista[índice]

// Expresiones - Define la precedencia de operadores (de mayor a menor)
expr: expr MUL expr #Mul            // Multiplicación: a * b
    | expr DIV expr #Div            // División: a / b
    | expr MOD expr #Mod            // Módulo: a % b
    | expr SUM expr #Sum            // Suma: a + b
    | expr MIN expr #Min            // Resta: a - b
    | expr GT expr  #Gt             // Mayor que: a > b
    | expr GET expr #Get            // Mayor o igual: a >= b
    | expr LT expr  #Lt             // Menor que: a < b
    | expr LET expr #Let            // Menor o igual: a <= b
    | expr EQ expr  #Eq             // Igual: a = b
    | expr NEQ expr #Neq            // No igual: a /= b
    | VAR           #Var            // Variable
    | STRING        #String         // Cadena: "texto"
    | NUM           #Num            // Número: 42 o -3.14
    | lista         #lst            // Lista: {1 2 3}
    | siz           #sz             // Tamaño: #lista
    | consult       #consul         // Consulta: lista[0]
    | NOTA          #Nota           // Nota musical: C4
    | LP expr RP    #Parens ;       // Paréntesis: (expr)

// Operador de tamaño para listas
siz: SIZE VAR;        // #lista - obtiene el tamaño de una lista
SIZE: '#';            // Símbolo de tamaño

// Notas musicales: C, D, E, F, G, A, B, opcionalmente seguidas de octava (0-9)
NOTA: [A-G][0-9]?;

// Nombres de procedimientos: deben empezar con mayúscula
PROCNAME: [A-Z][a-zA-Z0-9_]*;

// Delimitadores
LB: '|:';            // Inicio de bloque
RB: ':|';            // Fin de bloque
LP: '(';             // Paréntesis izquierdo
RP: ')';             // Paréntesis derecho
LS: '[';             // Corchete izquierdo
RS: ']';             // Corchete derecho

// Operadores aritméticos y de comparación
SUM: '+';            // Suma
MIN: '-';            // Resta
MUL: '*';            // Multiplicación
DIV: '/';            // División
MOD: '%';            // Módulo
EQ: '=';             // Igual
NEQ: '/=';           // No igual
GT: '>';             // Mayor que
LT: '<';             // Menor que
GET: '>=';           // Mayor o igual que
LET: '<=';           // Menor o igual que

// Identificadores y literales
VAR: [a-zA-Z][a-zA-Z0-9]*;                     // Variables: empiezan con letra
NUM: '-'?[0-9]+('.'[0-9]+)?;                   // Números: enteros o decimales
STRING: '"' ( '\\' . | ~('\\'|'"'))* '"';      // Cadenas: entre comillas dobles

// Comentarios y espacios en blanco (ignorados por el parser)
COMMENT: '###' ~[\r\n]* -> skip;               // Comentarios de línea: ### comentario
WS: [ \t\r\n]+ -> skip;                        // Espacios en blanco y saltos de línea
