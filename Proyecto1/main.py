set={}
comandos=[]
palabraUsada=''


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

#obtiene atibutos cargados y los ingresa a memoria
def automataAtrib(texto):

    estado=0
    palabraAux=''
    atributoAux=''
    diccionario={}
    contador=0
    objetos=[]

    file=open(texto, "r")
    entrada=file.read()

    for caracter in entrada:
        if caracter=='(' and estado==0:
            objetos=[]
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
            set[setID].append(diccionario)
            #objetos.append(diccionario)
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
            set[setID].append(diccionario)
            #objetos.append(diccionario)
            diccionario = {}
            estado=10
    #define atributos booleanos
        if estado==9 and not caracter==',':
            for letra in letras:
                if letra==caracter:
                    atributoAux+=caracter.lower()
        if estado==9 and caracter==',':
            diccionario[palabraAux]=atributoAux
            estado=2
            continue
        if estado==9 and caracter=='>':
            diccionario[palabraAux]=atributoAux
            set[setID].append(diccionario)
            #objetos.append(diccionario)
            diccionario = {}
            estado=10
            continue
    #termina objeto
        if estado==10 and caracter==',':
            estado=1
            continue
    #termina estructura
        if estado ==10 and caracter==')':
            #objetosAux=[]
            #objetosAux=set[setID]
            #objetosAux.append(objetos)
            estado=0
            continue
    file.close()

entrada='''count *;
sum edad,promedio,faltas;
report to reporte3 select * where edad != 44;
print in blue;
report tokens;
select * where marca = "mazda" and año >= 1996;
load into elementos files periodica.aon,periodica2.aon;
'''

#separa las palabras de archivo sqli
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
#separa las palabras del comando ingresado y las ingresa en un vector
def instruccion(texto):

    palComandoAux = ''
    global com
    com=[]
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

#contiene las funciones principales del programa
def principal():
    texto=''
    while True:
        print('Bienvenido, ingrese su comando: ')
        texto=input()
        instruccion(texto)
        verificaComando(com)
        texto=''
        #print(set)

setID=''
#verifica comando ingresado y lo procesa
def verificaComando(vector):
    global set
    global setID
    global palabraUsada
    estado=0
    for palabra in vector:
#create set
        if palabra.lower()=='create' and estado==0:
            estado=1
            continue
        if estado==1 and palabra.lower()=='set':
            estado=2
            continue
        if estado==2:
            set[palabra]=[]
            print('Se ha creado el ID ',palabra)
            estado=0
            continue
#load into
        if estado==0 and palabra.lower()=='load':
            estado=3
            continue
        if estado==3 and palabra.lower()=='into':
            estado=4
            continue
        if estado==4:
            setID=palabra
            estado=5
            continue
        if estado==5:
            automataAtrib(palabra)
            print('Se ha cargado '+palabra+' en '+setID)
            continue
#use set
        if estado==0 and palabra.lower()=='use':
            estado=6
            continue
        if estado==6 and palabra.lower()=='set':
            estado=7
            continue
        if estado==7:
            if palabra in set:
                palabraUsada=palabra
                estado=0
                print('Ahora esta utilizando el ID '+palabraUsada)
                continue
            else:
                print('El ID '+ palabra+' no se encuentra registrado')
                estado=0
                continue
#list atributes
        if estado==0 and palabra.lower()=='list':
            estado=8
            continue
        if estado==8 and palabra.lower()=='atributes':
            for atrib in set[palabraUsada][0]:
                print(atrib)
            estado=0
            continue
#max
        if estado==0 and palabra.lower()=='max':
            estado=9
            continue
        if estado==9:
            maximo=-5000000.0
            for max in set[palabraUsada]:
                if float(max[palabra]) >= maximo:
                    maximo=float(max[palabra])
            print (maximo)
            estado=0
            continue
#min
        if estado==0 and palabra.lower()=='min':
            estado=10
            continue
        if estado==10:
            minimo=50000000.0
            for min in set[palabraUsada]:
                if float(min[palabra]) <= minimo:
                    minimo=float(min[palabra])
            print (minimo)
            estado=0
            continue
#sum
        if estado==0 and palabra=='sum':
            estado=11
            continue
        if estado==11:
            suma=0.0
            for sum in set[palabraUsada]:
                suma+=float(sum[palabra])
            print(suma)
            estado=0
            continue
#count
        if estado==0 and palabra=='count':
            estado=12
            continue
        if estado==12:
            conteo=0
            for cont in set[palabraUsada]:
                if not cont[palabra]=='null':
                    conteo+=1
            print(conteo)
            estado=0
            continue

principal()