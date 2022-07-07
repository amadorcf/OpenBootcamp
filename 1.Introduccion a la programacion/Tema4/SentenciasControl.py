def es_positivo(numero_if):
    if numero_if < 0:
        print(f"IF: El numero {numero_if} es negativo.")
    else:
        print(f"IF: El numero {numero_if} es positivo.")


def bucle_while(numero_while):
    while numero_while <= 3:
        numero_while += 1
        print(f"BUCLE_WHILE: El numero es {numero_while}")


def simular_do_while(num):
    numero = 3
    contador = 1
    while True:
        contador += 1
        print("Bucle infinito")
        if num == numero:
            print(f"BUCLE_DO_WHILE: El numero es {num}")
            break
        if num != numero and contador > 8:
            break


def bucle_for(numero_for):
    n = 0
    for n in range(numero_for):
        print(f"BUCLE_FOR: El numero es {numero_for}")
        numero_for += 1


def simular_switch(num):
    if num:
        if num == 1:
            print("Es primavera")
        elif num == 2:
            print("Es verano")
        elif num == 3:
            print("Es otoño")
        elif num == 4:
            print("Es inviero")
        else:
            print("El numero no corresponde con ninguna estacion")


numero = int(input("Introduzca un numero entre -5 y 5: "))
print("")
es_positivo(numero)
print("")
bucle_while(numero)
print("")
simular_do_while(numero)
print("")
bucle_for(numero)
print("")
simular_switch(numero)
