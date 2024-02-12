print("Ingrese una nota de 0 a 100")

nota = input()
nota = int(nota)

if nota >= 94:
    gpa = 4.0
else:
    if nota >= 90 and nota <= 92:
        gpa = 3.8
    else:
        if nota >= 87 and nota <= 89:
            gpa = 3.3
        else:
            if nota >= 83 and nota <= 86:
                gpa = 3.0
            else:
                gpa = 0

print("Tu GPA es de:", gpa)
