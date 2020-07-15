import numpy as np

def sumar_triplicar(n1,n2):
    return (n1+n2)*3

def restar(n1,n2):
    return n1-n2

def cuadrado(n):
    return n*n

def raiz_cuadrada(n):
    return np.sqrt(n)

def num_par(n):
   if n%2==0:
       return "el número es par"