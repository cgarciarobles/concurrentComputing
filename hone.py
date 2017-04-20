import random


arreglo = ['a','a','a','a','a']

def procA(contador):
    arreglo[contador] = 'a'
    contador += 1
    return contador

def procB(contador):
    if contador == 0:
        print "El limite de bs esta definido por la cantidad de as"
    else:
        if arreglo[contador-1] == 'b':
            print "No pueden escribirse dos b seguidas"
        else:
            arreglo[contador] = 'b'
            contador += 1
    return contador

def procC(contador):
    if contador == 0:
        print "El limite de cs esta definido por la cantidad de as"
    else:
        if arreglo[contador-1] == 'c':
            print "No pueden escribirse dos c seguidas"
        else:
            arreglo[contador] = 'c'
            contador += 1
    return contador

contador = 0
while contador < 5:
    x = random.randint(0,2)
    if x == 0:
        contador = procA(contador)
    elif x == 1:
        contador = procB(contador)
    elif x == 2:
        contador = procC(contador)


print arreglo
