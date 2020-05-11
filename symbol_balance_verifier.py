from Stack import Stack

def syntax_verifier(expr):
    open = "<"
    close = ">"
    stack = Stack()
    tam = len(expr)
    if expr[0]!="<" or expr[tam-1]!=">":
        return False

    for c in expr:
        if c in open:
            stack.push(c)
        elif c in close:
            if stack.is_empty():
                return False
            else:
                if close.index(c) != open.index(stack.pop()):
                    return False

    return stack.is_empty()



