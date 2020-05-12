from symbol_balance_verifier import syntax_verifier as isBalance
def isXml(input):
    return True if input == "<xml>" else False
def isOpenTag(input): #<manito huachicol=vargas>, <manito>,
    tam = len(input)
    if isBalance(input) and tam>2:
        input = input[1:tam-1]
        aux = input.split(" ")
        tag = aux[0]
        attributes = aux[1:]
        if input[len(input)-1] == "/":
            return False
        if not tag[0].isalpha():
            return False
        if len(attributes)>0:
            for var in attributes:
                if not isInternalAttribute(var):
                    return False
            return True
        else:
            return True
    else:
        return False

def isCloseTag(input):
    tam = len(input)
    if tam > 3:
        first = input[:2]
        last = input[tam-1]
        if first == "</" and last == ">":
            tagName = input[2:tam-1].split(" ")
            if len(tagName)>1:
                return False
            elif len(tagName)==1:
                w = tagName[0]
                if w[0].isalpha():
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False
def isOpenClose(input): #<manito huachicol=vargas>, <manito>,
    tam = len(input)
    if isBalance(input) and tam>2:
        if input[tam-2] != "/":
            return False
        aux = input[1:tam-2].split(" ")
        tag = aux[0]
        attributes = aux[1:]
        if not tag[0].isalpha:
            return False
        if len(attributes)>0:
            for var in attributes:
                if not isInternalAttribute(var):
                    return False
            return True
        else:
            return True
    else:
        return False


def isInternalAttribute(exp):
    exp = exp.split("=")
    if len(exp)==2:
        w1 = exp[0]
        w2 = exp[1]
        cont = 0
        if not w1[0].isalpha():
            return False
        if len(w2)>=2:
            if w2[0] != "'" or w2[len(w2)-1] != "'":
                return False
            return True
        else:
            return False
    else:
        return False

exp = "</atributo>"
if isOpenTag(exp):
    print("openTag")
if isCloseTag(exp):
    print("closeTag")
if isOpenClose(exp):
    print("openClose")