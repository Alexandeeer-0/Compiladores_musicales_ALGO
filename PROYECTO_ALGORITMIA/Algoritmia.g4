// la estruct. base p mi chill de cojones:
grammar Algoritmia; //definimos el nombre de la gramática
root: procDef* EOF; //definimos el root de la gramática, aca especificamos que procDef puede estar 0 o mas veces y termina con EOF que es el fin del archivo.(end of file)  


//INS: definimos que inss puede estar 0 o mas veces. inss es una lista de instrucciones.
inss: ins*;
//definimos que ins puede ser una condición, un while, una entrada, una salida, un procedimiento, una asignación, o una reproducción. 
ins: (condition | while_)
    | (input_ | output_ | proc | assign | reprod) //input_ es una entrada, output_ es una salida, proc es un procedimiento, assign es una asignación, reprod es una reproducción.
    | (agregado | corte) ; 


// INPUT & OUTPUT:
input_: '<?>' VAR;      
output_: '<w>' expr+;   

// CONDITION & WHILE: (ahi dejo el flujo de la gramática pa que entiendan xdd, osea el significado de cada cosa)
condition: 'if' expr LB inss RB ('else' LB inss RB)?; 
//condition: if expresion |: instrucciones :| else |: instrucciones :|
while_: 'while' expr LB inss RB;                       
//while: while expresion |: instrucciones :|

// REPROD:
reprod: REPROD expr;
// Reproduccion de nota: (:) nota
REPROD: '(:)';         

// AGREGADO & CORTA:
agregado: VAR AGREGADO expr;        
// Agregar elemento: lista << elemento
AGREGADO: '<<';         

// CORTA:
corte: CORTA VAR LS expr RS;        
//Corte:  8<  VARIABLE [expresion]
CORTA: '8<';                   

// PROC
procDef: PROCNAME paramsId LB inss RB;    
// procDef: PROC param1 param2 |: instrucciones :|
proc: PROCNAME paramsExpr (expr)*;  

// Asignacion:
assign: VAR ASSIGN expr;   
// assign: variable <- expresión
ASSIGN: '<-';            

//PARAMS:
paramsId: (VAR)*;
paramsExpr: (expr)*;

// Listas y acceso
lista : '{' expr* '}';// Definición de lista: {1 2 3}
consult: VAR LS expr RS;

// Expresiones - Define la precedencia de operadores
expr: expr MUL expr #Mul            // Multiplicación
    | expr DIV expr #Div            // División
    | expr MOD expr #Mod            // Modulo
    | expr SUM expr #Sum            // Suma
    | expr MIN expr #Min            // Resta
    | expr GT expr  #Gt             // Mayor que
    | expr GET expr #Get            // Mayor o igual
    | expr LT expr  #Lt             // Menor que
    | expr LET expr #Let            // Menor o igual
    | expr EQ expr  #Eq             // Igual
    | expr NEQ expr #Neq            // No igual
    | VAR           #Var            // Variable
    | STRING        #String         // Cadena
    | NUM           #Num            // Numero
    | lista         #lst            // Lista
    | siz           #sz             // Tamaño
    | consult       #consul         // Consulta
    | NOTA          #Nota           // Nota musical
    | LP expr RP    #Parens ;       // Paréntesis

// SIZE:
siz: SIZE VAR;// #lista - obtiene el tamaño de una lista
SIZE: '#';    

// Notas musicales: C, D, E, F, G, A, B
NOTA: [A-G][0-9]?;

// Nombres de procedimientos: deben empezar con mayúscula si o si
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


// NOLVIDAR: * -> Cero o mAs ocurrencias del elemento anterior

// Identificadores y literales
VAR: [a-zA-Z][a-zA-Z0-9]*;                     
// Variables: empiezan con letra, despues pueden venir 0 o mas caracteres que sean letras o números

NUM: '-'?[0-9]+('.'[0-9]+)?;                   
// Números:Puede tener opcionalmente un signo negativo al inicio, Debe tener uno o más dígitos, Opcionalmente puede tener un punto decimal seguido de más dígitos Y  todo gracias al '?'

STRING: '"' ( '\\' . | ~('\\'|'"'))* '"';      
// Cadenas: Comienza con comilla doble.  estas son '\\' secuencia de escape y el punto '.' es cualquier caracter excepto '\\' o '"'. Y ~('\\'|'"'): Cualquier carácter excepto backslash o comilla doble. Termina con comilla doble

// Comentarios y espacios en blanco
COMMENT: '###' ~[\r\n]* -> skip;               // Comentarios de línea: ### comentario
WS: [ \t\r\n]+ -> skip;                        // Espacios en blanco y saltos de línea
