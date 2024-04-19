
def promedio(notas):
    n = len(notas)
    
    suma = 0
    for num in notas:
        suma += num
        
    x = suma / n
    
    return x
    
    

estudiantes = [
    {"nombre": "ERICK MARROQUIN", "carnet": "123456", "notas": [100, 98, 89]},
    {"nombre": "FRANCISCO RODRIGUEZ", "carnet": "987654", "notas": [100, 100, 99]},
]


opc = ""

while opc != "6":
    print()
    print("=== NOTAS UVG ===")
    print("1. Agregar estudiante")
    print("2. Agregar nota")
    print("3. Eliminar estudiante")
    print("4. Promedio estudiante")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print()
    
    opc = input("Seleccione una opción: ")
    print()
    
    if opc == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        carnet = input("Ingrese el número de carnet: ")
        notas = []
        
        estudiante = {
            "nombre": nombre,
            "carnet": carnet,
            "notas": notas
        }
        
        estudiantes.append(estudiante)
        
        
    elif opc == "2":
        carnet = input("Ingrese el número de carnet: ")
        
        for e in estudiantes:
            if e["carnet"] == carnet:
                nota = int(input("Ingrese la nota: "))
                
                e["notas"].append(nota)
        
    elif opc == "3":
#         carnet = input("Ingrese el número de carnet: ")
#         
#         for e in estudiantes:
#             if e["carnet"] == carnet:
#                 estudiantes.remove(e)

        nombre = input("Ingrese el nombre del estudiante: ")
        
        for e in estudiantes:
            if e["nombre"].lower() == nombre.lower():
                estudiantes.remove(e)
        
        
    elif opc == "4":
        carnet = input("Ingrese el número de carnet: ")
        
        for e in estudiantes:
            if e["carnet"] == carnet:
                x = promedio(e["notas"])
                
                print("El promedio del estudiante es: ", x)
                
    elif opc == "5":
        print("Listado de estudiantes:")
        
        for e in estudiantes:
            print(e)
        
    elif opc == "6":
        print("Nos vemos pronto")
        
    else:
        print("Opción inválida... Intentalo nuevamente.")
    
        
        
        
        
        
        