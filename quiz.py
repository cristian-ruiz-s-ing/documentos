from sys import stdin
import libreriacomplejos
import numpy as np
import matplotlib.pyplot as plt

def f(x,c):
    y= libreriacomplejos.suma(libreriacomplejos.mult(x,x),c)
    if libreriacomplejos.modulo(y)> 2:
        return False

    else:
        return True

'''def graficar():
    plano= np.zeros((400,700))

    for parte_real in range(700):
        for parte_imaginaria in range(400):
            c=((parte_real/200)-2.5,(parte_imaginaria/200)-1)
            pertenece,color=funcion((0,0),c)
            if pertenece==True:
                plano[parte_imaginaria][parte_real]=color
            else:
                plano[parte_imaginaria][parte_real]=color

    plt.figure(figsize=(10,10))
    plt.imshow(plano,'magma')
    plt.show()
    
'''
def main():
    c=tuple(stdin.readline().split(','))
    x=(0,0)
    count=30
    resultado=True
    while count > 0:
        resultado= resultado and f(x,c)
        x= libreriacomplejos.suma(libreriacomplejos.mult(x,x),c)
        print(resultado)
        if resultado == False:
            break
        count-=1
    
    print(resultado)
    
    

main()
