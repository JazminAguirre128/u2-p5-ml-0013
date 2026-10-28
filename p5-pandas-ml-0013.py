import numpy as np
import pandas as pd
# Meredith Aguirre NC = 0013
## Datos natriz 4 x 3
datos_alumnos = [
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 50, 2]
]
# Poner nombre a las columnas 
# Y almacenar la tabla en la variable df DataFrame
print("------ Datos a partir de una matriz 4 x 3 ------")
df = pd.DataFrame(datos_alumnos, columns = ['ci', 'marcas', 'paquete'])
print(df)
# Datos a partir de un diccionario
print("------ Datos a partir de un diccionario ------")
alumno_diccionario = {
    "Nombre":["Ricardo", "Aldahir", "Iram", "Anais", "William", "Caleb"],
    "Califa":[60, 70, 100, 90, 50, 77],
    "Edad":[16, 18, 16, 16, 16, 15]
}      
estudiantes = pd.DataFrame(alumno_diccionario)
print(estudiantes)
print("Meredith Aguirre NC = 0013")