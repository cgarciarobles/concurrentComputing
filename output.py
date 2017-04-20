import random
import os

arreglo = [10,20,30,40,50]
banderaBloqueado = False

def leccA():
    global banderaBloqueado
    if (banderaBloqueado == False):
        print arreglo
    else:
        print "El acceso al recurso no es posible, esta bloqueado por turno de escritura de un proceso anterior"
        banderaBloqueado = False

def escA():
    global banderaBloqueado
    if (banderaBloqueado == False):
        print arreglo
        pos = input('Escriba la posicion del arreglo que desea cambiar: ')
        num = input('Escriba el numero a modificar: ')
        arreglo[pos] = num
        banderaBloqueado = True
    else:
        print "El acceso al recurso no es posible, esta bloqueado por turno de escritura de un proceso anterior"


def leccB():
    global banderaBloqueado
    if (banderaBloqueado == False):
        print arreglo
    else:
        print "El acceso al recurso no es posible, esta bloqueado por turno de escritura de un proceso anterior"
        banderaBloqueado = False

def escB():
    global banderaBloqueado
    if (banderaBloqueado == False):
        print arreglo
        pos = input('Escriba la posicion del arreglo que desea cambiar: ')
        num = input('Escriba el numero a modificar: ')
        arreglo[pos] = num
        banderaBloqueado = True
    else:
        print "El acceso al recurso no es posible, esta bloqueado por turno de escritura de un proceso anterior"


def leccC():
    global banderaBloqueado
    if (banderaBloqueado == False):
        print arreglo
    else:
        print "El acceso al recurso no es posible, esta bloqueado por turno de escritura de un proceso anterior"
        banderaBloqueado = False

def escC():
    global banderaBloqueado
    if (banderaBloqueado == False):
        print arreglo
        pos = input('Escriba la posicion del arreglo que desea cambiar: ')
        num = input('Escriba el numero a modificar: ')
        arreglo[pos] = num
        banderaBloqueado = True
    else:
        print "El acceso al recurso no es posible, esta bloqueado por turno de escritura de un proceso anterior"

while True:
    print '\n\n'
    print "Menu:"
    print "\t1) Proceso Lectura A"
    print "\t2) Proceso Lectura B"
    print "\t3) Proceso Lectura C"
    print "\t4) Proceso Escritura A"
    print "\t5) Proceso Escritura B"
    print "\t6) Proceso Escritura C"
    print "\t7) Salir"
    opcion = input('Escriba el numero de la opcion que desea realizar: ')
    if opcion == 1:
        os.system('clear')
        leccA()
    if opcion == 2:
        os.system('clear')
        leccB()
    if opcion == 3:
        os.system('clear')
        leccC()
    if opcion == 4:
        os.system('clear')
        escA()
    if opcion == 5:
        os.system('clear')
        escB()
    if opcion == 6:
        os.system('clear')
        escC()
    if opcion == 7:
        break;
