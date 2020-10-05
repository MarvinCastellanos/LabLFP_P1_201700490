#SimpleQL CLI
simpleQL CLI es un programa que permite el almacenamiento y manipulación de datos atraves de una linea de comando.

Para poder utilizar el programa debe de conocerse su sintaxis y forma de uso.

##Notación e instrucciones preliminares:
###< >
####Estos caracteres indican que su contenido es determinado por el usuario, por ejemplo, < ID > podría tomar como valores válidos: Estudiantes, Mascotas, Clientes, etc.
###+
####Indica que el elemento puede venir de una a muchas veces.
###Palabras en mayúscula
####Indican keywords que pertenecen a SimpleQL
###[]
####Indican que su contenido es opcional

##Comandos
###CREATE SET < ID >
###LOAD INTO < set_id > FILES < id > [ , <id> ] +
###USE SET < set_id >
###SELECT < atributo > [ , <atributo>] + [ WHERE < condiciones > ]
###LIST ATTRIBUTES
###PRINT IN <color>
###MAX < atributo > | MIN < atributo >
###SUM < atributo > [, <atributo> ] +
###COUNT < atributo > [, < atributo > ] +
###REPORT TO < id > < comando >
###SCRIPT < direccion > [, < direccion > ]
###REPORT TOKENS

##Consideraciones de la CLI

##Alternative Object Notation (AON)

##SimpleQL Regex

##SimpleQL Script (Siql)