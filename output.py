import random

array = ['a','a','a','a','a']
global contA
contA = 0

def procA(cont):
    array[cont] = 'a'
    contA = contA + 1
    cont = cont + 1
    return cont


def procB(cont):
    if cont > 0:
        if array[cont-1] == 'c' and contO <= contA:
            array[cont] = 'b'
            cont = cont + 1
            contO = contO + 1
            return cont

def procC(cont):
    if cont > 0:
        if array[cont-1] == 'b' and contO <= contA:
            array[cont] = 'c'
            cont = cont + 1
            contO = contO + 1
            return cont


cont = 0
while cont < 5:
    global contO
    x = random.randint(0,2)
    if x == 0:
        cont = procA(cont)
    elif x == 1:
        cont = procB(cont)
    elif x == 2:
        cont = procC(cont)

print array
