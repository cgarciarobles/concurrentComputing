import random

"""
===============================================================
Carlos Garcia Robles 15744-14
GitHub @cgarciarobles
===============================================================
"""

arreglo = ['a','a','a','a','a']
contadorA = 0
contadorO = 0


""" El procedimiento A es mas simple, ya que solo escribe esta letra en el arreglo, en la posicion del contador
# y suma a un contador de as para que las b y c nunca sobrepasen su cantidad. """
def procA(contador):
    global contadorA
    arreglo[contador] = 'a'
    contador += 1
    contadorA += 1
    return contador


""" El procedimiento B y C funcionan de la misma manera, pero son inversos en la letra que escriben
    y en la comparacion no pueden ser escritos en la primera posicion porque sobrepasarian en cantidad
    a las A. Al ser escritas en cualquier posicion que no sea la primera, hacen una comparacion con la
    posicion anterior del contador para que no se escriban dos seguidas. De igual forma, se hace una
    comparacion con el contador de As para no exceder en cantidad lo que escriba alguna de estas funciones."""
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



""" El contador define un ciclo de uno a cinco y al cumplirse uno de los procedimientos,
    es decir, al tener un buen manejo de la concurrencia en los procedimientos, se suma uno. """

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
