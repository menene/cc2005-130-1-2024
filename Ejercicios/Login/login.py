import pandas as pd

usuarios = pd.read_csv("usuarios.csv")

logged_in = False

while not logged_in:
    print("==========================")
    print("LOGIN 🔒")
    print()
          
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    print()
          
    check = usuarios.loc[(usuarios["Usuario"] == user) & (usuarios["Clave"] == password)]
    
    if len(check) != 1:
        print("🛑 Usuario incorrecto ✋🏼")
        print()
        
    else:
        print("Bienvenido al sistema super secreto! 🤫")
        logged_in = True