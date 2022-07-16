peso = int(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))

imc = peso / estatura ** 2

print(f"Su IMC es: {round(imc, 2)}")
