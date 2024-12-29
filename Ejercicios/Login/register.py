import pandas as pd

usuarios = pd.read_csv("usuarios.csv")


name = input("Ingrese su nombre: ")
username = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

usr = {"Usuario": username, "Nombre": name, "Clave": password}

usuarios._append(usr, ignore_index=True)

usuarios.to_csv("usuarios2.csv", index=False)
