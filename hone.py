import random


arreglo = ['a','a','a','a','a']
contadorA = 0
contadorO = 0

def procA(contador):
    global contadorA
    arreglo[contador] = 'a'
    contador += 1
    contadorA += 1
    return contador


def procB(contador):
    global contadorA
    global contadorO
    if contador == 0:
        print "El limite de bs esta definido por la cantidad de as"
    else:
        if arreglo[contador-1] == 'b':
            print "No pueden escribirse dos b seguidas"
        else:
            if contadorA > contadorO:
                arreglo[contador] = 'b'
                contador += 1
                contadorO += 1
            else:
                print "El limite esta definido por la cantidad de as"
    return contador


def procC(contador):
    global contadorA
    global contadorO
    if contador == 0:
        print "El limite de cs esta definido por la cantidad de as"
    else:
        if arreglo[contador-1] == 'c':
            print "No pueden escribirse dos c seguidas"
        else:
            if contadorA > contadorO:
                arreglo[contador] = 'c'
                contador += 1
                contadorO += 1
            else:
                print "El limite esta definido por la cantidad de as"
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
