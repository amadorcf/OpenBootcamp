def esBisiesto(año):
    if (año % 400 == 0) and (año % 100 == 0):
        return print(f"{año} es un año bisiesto")
    elif (año % 4 == 0) and (año % 100 != 0):
        return print(f"{año} es un año bisiesto")
    else:
        return print(f"{año} no es bisiesto")


esBisiesto(año=int(input("Introduzca un año: ")))
