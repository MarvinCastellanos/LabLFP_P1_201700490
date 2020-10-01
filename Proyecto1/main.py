set=[]
objetos=[]

tokenList={
    "tk_parenA":'(',
    "tk_parenC":')',
    "tk_menQ":'<',
    "tk_mayQ":'>',
    "tk_corchA":'[',
    "tk_corchC":']',
    "tk_igual":'=',
    "tk_coma":',',
    "tk_comilla":'"'
}

letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","-",
        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","_"]

numeros=["1","2","3","4","5","6","7","8","9","0"]

caracter='['
if caracter== tokenList['tk_corchA']:
    print(tokenList['tk_corchA'])