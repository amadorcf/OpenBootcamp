import math

base = float(input("Base del triangulo: "))
altura = float(input("Altura del triangulo: "))


def areaTriaungulo(altura, base):
    resultado = base * altura
    return print(f"El area del triangulo es igual a {resultado} m2\n")

def areaCirculo():
    radio = float(input("Radio del circulo: "))
    total_area_circulo = math.pi * (radio ** 2)
    return print(f"El area del circulo es igual a {round(total_area_circulo, 2)} m2")


areaTriaungulo(base, altura)
areaCirculo()
