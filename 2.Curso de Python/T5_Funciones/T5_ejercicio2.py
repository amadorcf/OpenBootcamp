def esPrimo(num):
    if num == 1:
        return print("No es primo")
    for n in range(2, num):
        if num % n == 0:
            return print("No es primo!")
    return print("Es primo")


esPrimo(int(input("Introduzca un numero: ")))
