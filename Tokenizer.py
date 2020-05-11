from symbol_balance_verifier import syntax_verifier as isBalance
def tokens(word):
    lista = list()
    while len(word)>0:
        char = word[0]
        token = ""
        if char == "<":
            token = char
            while True:
                word = word[1:]
                token = token + word[0]
                if word[0]==None or word[0]==">":
                    break
            #Termina el ciclo while con el caracter ">" insertado en var
            lista.append(token) #agregamos el token
            if len(word)>0:
                word = word[1:] #eliminamos de la cadena el primer elemento, el cual era el símbolo ">"
        else:
            token = ""
            while word[0]!="<":
                token = token + word[0]
                word = word[1:]
                if len(word)<=0:
                    break
            lista.append(token)
    return lista
def tagName(exp):
    if isBalance(exp) and len(exp)>2:
        exp = exp[1:len(exp) - 1]
        exp = exp.split(" ")
        return exp[0]
    else:
        return "@@@@error"

#print(tokens("< querida wowow ffml> mamasa <>"))
#print(tagName("<hi what ever>"))