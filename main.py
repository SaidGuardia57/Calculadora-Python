import Operaciones

while True:
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
    except:
        print("Error: ingrese números válidos")
        continue

    print("Seleccione operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Opción: ")

    if opcion == "1":
        resultado = Operaciones.sumar(a, b)
    elif opcion == "2":
        resultado = Operaciones.restar(a, b)
    elif opcion == "3":
        resultado = Operaciones.multiplicar(a, b)
    elif opcion == "4":
        resultado = Operaciones.dividir(a, b)
    else:
        resultado = "Opción inválida"

    print("Resultado:", resultado)

    repetir = input("¿Quieres hacer otra operación? (s/n): ")
    if repetir.lower() != "s":
        break
