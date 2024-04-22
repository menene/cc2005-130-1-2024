import pandas as pd

df = pd.DataFrame({
    "Hoja de trabajo 1": [80, 85, 75, 40, 0],
    "Hoja de trabajo 2": [90, 90, 75, 61, 100],
    "Hoja de trabajo 3": [80, 80, 0, 50, 85],
})

# Imprimir el dataframe en pantalla
# print(df)

# Imprime el tamaño del dataframe. Filas y columnas
# print(df.shape)

# Imprime la descripción estadistica del data frame
# print(df.describe())

# print(df.mean())
# print(df.max())
# print(df.min())
# print(df.std())

# print("---")
# print(df["Hoja de trabajo 1"])
# print(df["Hoja de trabajo 1"][0])

estudiantes = pd.read_csv('estudiantes.csv')
print(estudiantes)













