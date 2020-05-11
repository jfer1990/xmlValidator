from symbol_balance_verifier import syntax_verifier as isBalance
def isXml(input):
    return True if input == "<xml>" else False
def isOpenTag(input): #<manito huachicol=vargas>, <manito>,
    tam = len(input)
    if isBalance(input) and tam>2:
        aux = input[1:tam-1].split(" ")
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

def isCloseTag(input):
    size = len(input)
    if size>=4:
        first = input[0:2]
        last = input[size - 1]
        middle = input[2:size-1]
        if first != "</" or last != ">":
            return False
        for char in middle:
            if char == " ":
                return False
        return True
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
        for c in w1:
            if not c.isalpha():
                return False
        if len(w2)>=2:
            if w2[0] != "'" or w2[len(w2)-1] != "'":
                return False
            return True
        else:
            return False
    else:
        return False

print(isOpenTag("<tagElement>"))
print(isOpenTag("<tagElement attribute='value'>"))
print(isOpenClose("<tagElement attribute='value'/>"))

