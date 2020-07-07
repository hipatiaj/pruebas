import numpy as np
import pandas as pd
from sumar import sumar

print(" hello Pandas")

datos={"nombres":["samuel","brenda","vivi"],"edades":[24,24,24]}
df=pd.DataFrame(datos)
print(df)

print(sumar(3,4),"sumando 3 +4")
print("hello python")

dataframe_csv2=pd.read_csv("C:/Users/Samuel Cueva/Desktop/actividad 1.csv")
