grammar bazilio;
root: procDef* EOF;//definion de orden de procedimiento, * = cierre de clean, 'EOF = end of file'
inss: ins*; // definimos para las instrucciones que ins= instrucciones, esto esta en "especificacion del lenguaje" en el PDF.
//ins* de 0 a mas instrucciones

//disponemos de 9 instrucciones en total
ins: (condition | while_) //aca estamos especificando las instruciones como: condiciones, while
    | (input_ | output_ | proc | assign | reprod) //entrada, salida., procedimiento, asignicacion, reproduccion
    | (agregado_ | corte);

input_: '<?>' VAR;
output_: '<w>' expr+; //aca en el output definimos la salida de 1 a mas expresiones

condition: 'if' expr LB  inss RB ('else' LB inss RB)?; //da opcionalidad con el ELSE, osea si es que hay else ahi está, sino pues no pasa nada
//el '?' solo hace reconocimiento a la estructura dentro del ().
while_: 'while' expr LB inss RB;
assign: VAR ASSIGN expr;
ASSIGN: '<-'; //este es un token (MAYUS 1era Letra) el cual asigna el simbolo '<-' a ASSIGN.



//definicion de procedimiento:
PROCNAME: [A-Z][a-zA-Z0-9_]*; //cierre de clean que significa que puedes tener de 0 a mas secuencias
procDef: PROCNAME paramsId LB inss RB; //LB = LEFT BLOCK = BLOQUE IZQUIERDO, RB= RIGHT BLOCK
proc: PROCNAME paramsExpr;
//procDef:'NOMBRE PROCEDIMIENTO' 'LISTA DE SUS PARAMETROS' 'ABERTURA DEL BLOQUE' 'SECUENCIA DE INSTRUCCIONES' 'CIERRE DE BLOQUE';

paramsId: (VAR)*; //definimos el procedimiento, si o si debe comenzar con una mayuscula. '* = 0 a mas'. esto es una Lista de VARIABLES
paramExpr: (expr)*; //isnitruccion que define como parte del Proc


//asignacion de reproduccion
reprod: REPROD expr;
REPROD: '(:)'; //asignacion de '(:)' como REPROD para reprod. Linea de arriba xd


LB: '|:'; //INICIO DE LA SEC DE INSTRUCCIONES. LB: '|:'


RB: ':|'; //FIN DE LA SEC DE INST. RB: ':|'

//las variables empiezan si o si con minuscula
VAR: [a-zA-Z] [a-zA-Z-9]*;


