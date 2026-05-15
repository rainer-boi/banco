
while True:
    nombre=input("Ingrese nombre: ")
    if len(nombre)>=3 and nombre.isalpha():
        break
    else:
        print("Nombre mínimo 3 caracteres y sin números")

while True:
    try:
        edad=int(input("Ingrese edad: "))
        if edad>=18 and edad<=80:
            break
        else:
            print("Edad entre 18 y 80")
    except:
        print("Ingrese edad numérica")

while True:
    nickname=input("Ingrese apodo: ")
    if len(nickname)>=3 and not nickname in ' ':
        break
    else:
        print("Largo mínimo 3 y sin espacios en blanco")

while True:
    sexo=input("Ingrese sexo: ").upper()
    if sexo in [F, M]:
        break
    else:
        print("Solo F o M")
contra=input("Ingrese contraseña: ")
semestre=int(input("En qué semestre está: "))