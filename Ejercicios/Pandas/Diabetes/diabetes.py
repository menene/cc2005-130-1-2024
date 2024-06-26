# -*- coding: utf-8 -*-
"""Diabetes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yru1Heve0eJZQQr-2E90lHHM7-ifN4kI

# Diabetes

Estos datos vienen del National Institute of Diabetes and Digestive and Kidney Diseases. Fue generado para predecir si un paciente va a desarrollar diabetes dadas ciertos diagnostigos realizados.

Para estos datos todos los pacientes son mujeres de al menos 21 años de descendencia India.

source: https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset

Importación de Pandas para el análidis de los datos.
"""

import pandas as pd

"""Leer del archivo CSV (Data set)"""

df = pd.read_csv("diabetes.csv")

"""Verificamos la forma de los datos:"""

print(df.shape)

"""Imprimir el DataFrame:"""

print(df)

"""## Análisis exploratorio

Primero veamos que factores están presentes en las mujeres con diabetes:
"""

positivas = df.loc[df["Outcome"] == "Yes"]

print(positivas.describe())

"""Tien más sentido ver el promedio nada más de los factores:"""

print(positivas[["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]].mean())

"""Con estos promedios podemos encontrar a las pacientes negativas que están en alto riesgo:"""

riesgo = df.loc[(df["Outcome"] == "No") & ((df["Glucose"] >= 141) & (df["Insulin"] >= 100) & (df["BloodPressure"] >= 70) & (df["BMI"] >= 35))]

print(riesgo)

print(riesgo.describe())

"""Tenemos 4 factores que determinan el riesgo de diabetes: glucosa, insulina, presión arterial y el índice de masa corporal.

Agreguemos una columna nueva que sea la suma de los 4 factores.
"""

df["Factors"] = df["Glucose"] + df["Insulin"] + df["BloodPressure"] + df["BMI"]

print(df)

"""Analicemos a mayor profundidad esta columna"""

print(df[["Factors"]].describe())

"""Ahora podemos agregar una columna adicional con el riesgo de padecer diabetes. Para este caso vamos a usar la siguiente escala de porcentajes:

Si el valor de Factores está por debajo de la media entonces decimos que el riesgo es bajo. De lo contrario el riesgo es alto.

Para esto vamos a crear una función para calcular el riesgo y el resultado de la misma la vamos a aplicar a nuestra nueva columna.
"""

def calculate_risk(factor):
  if factor >= 200:
    return "High"
  else:
    return "Low"

df["Risk"] = df["Factors"].apply(calculate_risk)

# print(df["Glucose"][1])
print(df)

"""Veamos si tiene sentido nuestra función:"""

falsos_positivos = df.loc[(df["Outcome"] == "Yes") & (df["Risk"] == "Low")]

print(falsos_positivos.shape)

"""Con esto podemos escribir nuestro nuevo DataFrame con las columnas creada."""

df.to_csv('diabetes2.csv', index=False)

"""## Intro a gráficas

La función value counts nos va a dar la cantidad de valores que existe en una columna específica luego de agrupar.

Agupemos por cantidad de embarazos y determinemos la relación que existe con la diabetes.
"""

preg_diabetes = df.groupby('Pregnancies')['Outcome'].value_counts()

print(preg_diabetes)

"""Para mejorar la legibilidad podemos usar la función unstack"""

preg_diabetes = preg_diabetes.unstack()

print(preg_diabetes)

"""Con esta información podemos generar nuestra primera gráfica pero primero debemos importar las librerías necesarias."""

import matplotlib.pyplot as plt

preg_diabetes.plot(kind="bar", title="Cantidad de embarazos vs Diabetes", grid=True, stacked=False, rot=0)
plt.legend(title='Dx Diabetes', loc='upper right')
plt.xlabel('Embarazos')
plt.ylabel('Mujeres')
plt.show()