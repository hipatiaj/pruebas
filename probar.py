import numpy as np
import pandas as pd
<<<<<<< HEAD
from sumar import sumar,restar,dividir,cuadrado,raiz_cuadrada
=======
from sumar import sumar,restar,dividir,cuadrado,raiz_cuadrada
>>>>>>> test3

print(" hello Pandas")

datos={"nombres":["samuel","brenda","vivi"],"edades":[24,24,24]}
df=pd.DataFrame(datos)
print(df)

print(sumar_triplicar(3,4),"sumando 3 +4")
print("hello python")

print(restar(8,5))
<<<<<<< HEAD
print(dividir(10,2))
print(cuadrado(4))
print(raiz_cuadrada(16))
=======
print(dividir(10,2))
print(cuadrado(4))
print(raiz_cuadrada(16))
>>>>>>> test3
dataframe_csv2=pd.read_csv("C:/Users/Samuel Cueva/Desktop/actividad 1.csv")
print(dataframe_csv2)
