from Tokenizer import tokens, tagName
from Stack import Stack
from Predicates import *
#Configuración:
path = '/Users/jfer1990/Documents/Asesorias/Algoritmos/Rodrigo/xmlValidator'
nameFile = 'xmlUno.xml'
fileObject = open(path+"/"+nameFile,"r")


#Creación variables
contenidoXML = fileObject.read() #Lee y almacena el documento de un archivo en la variable xmlContent sin saltos de línea


#funciones:
def validarXML(string):
    xmlContent = tokens(string)
    stack = Stack()
    bandera = False

    for elemento in xmlContent:
        if elemento =="\n":
            continue
        if not isXml(elemento):
            if not isOpenTag(elemento):
                if not isCloseTag(elemento):
                    if not isOpenClose(elemento):
                        if stack.is_empty():
                            return False
                        elif not isOpenTag(stack.top()):
                            return False
                else:
                    elemento = tagName(elemento)
                    if not stack.is_empty():
                        if elemento != tagName(stack.pop()):
                            return False
            else:
                stack.push(elemento)
        else:
            bandera = True
    return bandera

#Codigo:
print(validarXML(contenidoXML))
