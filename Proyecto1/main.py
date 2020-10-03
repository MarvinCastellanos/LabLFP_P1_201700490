set=[]
objetos=[]
comandos=[]


letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","-",
        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","_"]

numeros=["1","2","3","4","5","6","7","8","9","0",".","+","-"]

entrada='''(
    <
        [atributo_numerico] = 45.09,
        [atributo_cadena] = "hola mundo",
        [atributo_booleano] = true
    >,
    <
        [atributo_numerico] = 4,
        [atributo_cadena] = "adios mundo",
        [atributo_booleano] = faLse,
        [atributo_numericos] = 478
    >,
    <
        [atributo_numerico] = -56.4,
        [atributo_cadena] = "este es otro ejemplo, las cadenas pueden ser muy largas",
        [atributo_booleano] = false,
        [atributo_cadenas] = "hola mundo"
    >
)'''

def automataAtrib(texto):
    estado=0
    palabraAux=''
    atributoAux=''
    diccionario={}
    contador=0

    for caracter in texto:
        if caracter=='(' and estado==0:
            estado=1
            continue
    #define objetos
        if estado==1 and caracter=='<':
            estado=2
            continue
    #define nombre de atributos
        if estado==2 and caracter=='[':
            palabraAux = ''
            atributoAux = ''
            estado=3
            continue
        if estado==3 and not caracter==']':
            palabraAux+=caracter
            continue
        if estado ==3 and caracter==']':
            estado=4
            continue
        if estado==4 and caracter=='=':
            estado=5
            continue
    #define atributos strings
        if estado==5 and caracter=='"':
            estado=6
            continue
        if estado==6 and not caracter=='"':
            atributoAux+=caracter
            continue
        if estado==6 and caracter=='"':
            estado=7
            continue
        if estado==7 and caracter==',':
            diccionario[palabraAux]=atributoAux
            estado=2
            continue
        if estado==7 and caracter=='>':
            diccionario[palabraAux]=atributoAux
            objetos.append(diccionario)
            diccionario={}
            estado=10
    #define atributos numericos
        if estado==5:
            for numero in numeros:
                if numero == caracter and estado==5:
                    estado=8
            for letra in letras:
                if letra==caracter and estado==5:
                    estado=9
                    break
        if estado==8 and not caracter==',':
            for numero in numeros:
                if numero == caracter:
                    atributoAux+=caracter
        if estado==8 and caracter==',':
            diccionario[palabraAux]=atributoAux
            estado=2
            continue
        if estado==8 and caracter=='>':
            diccionario[palabraAux]=atributoAux
            objetos.append(diccionario)
            diccionario = {}
            estado=10
    #define atributos booleanos
        if estado==9 and not caracter==',':
            for letra in letras:
                if letra==caracter:
                    atributoAux+=caracter.lower()
        if estado==9 and caracter==',':
            #print(palabraAux)
            diccionario[palabraAux]=atributoAux
            estado=2
            continue
        if estado==9 and caracter=='>':
            diccionario[palabraAux]=atributoAux
            objetos.append(diccionario)
            diccionario = {}
            estado=10
            continue
    #termina objeto
        if estado==10 and caracter==',':
            estado=1
            continue
    #termina estructura
        if estado ==10 and caracter==')':
            estado=0
            continue

entrada='''count *;
sum edad,promedio,faltas;
report to reporte3 select * where edad != 44;
print in blue;
report tokens;
select * where marca = "mazda" and año >= 1996;
load into elementos files periodica.aon,periodica2.aon;
'''
def sqli(texto):
    palComandoAux=''
    comando=[]
    for caracter in texto:
        for letra in letras:
            if letra==caracter:
                palComandoAux+=caracter
                break
        for numero in numeros:
            if numero==caracter:
                palComandoAux+=caracter
                break
        if caracter=='*' or caracter=='=' or caracter=='!' or caracter=='>' or caracter =='<':
            palComandoAux+=caracter
        if caracter==',' or caracter==' ' or caracter=='=' or caracter==';':
            if not palComandoAux=='':
                comando.append(palComandoAux)
                palComandoAux=''
        if caracter==';':
            comandos.append(comando)
            comando=[]
com=[]
def instruccion(texto):
    palComandoAux = ''
    global com
    for caracter in texto:
        for letra in letras:
            if letra == caracter:
                palComandoAux += caracter
                break
        for numero in numeros:
            if numero == caracter:
                palComandoAux += caracter
                break

        if caracter==',' or caracter==' ' or caracter=='=' or caracter==';' or caracter=='<' or caracter=='>':
            if not palComandoAux=='':
                com.append(palComandoAux)
                palComandoAux=''
        if caracter=='*' or caracter=='=' or caracter=='!' or caracter=='>' or caracter =='<':
            palComandoAux+=caracter
    print (com)


def principal():
    print('Bienvenido, ingrese su comando: ')
    texto=input()
    #instruccion(texto)

sqli(entrada)

for comando in comandos:
    print (comando)
#principal()