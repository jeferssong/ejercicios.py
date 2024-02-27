#14 area de un circulo con radio dado

import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

def main():
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        if radio < 0:
            print("El radio no puede ser negativo.")
        else:
            area = calcular_area_circulo(radio)
            print("El área del círculo con radio", radio, "es:", area)
    except ValueError:
        print("Error: Por favor ingrese un número válido para el radio.")

if __name__ == "__main__":
    main()




# 17 concatenacion de dos cadenas
    

def concatenar_cadenas():
    cadena1 = input("Ingrese la primera cadena de texto: ")
    cadena2 = input("Ingrese la segunda cadena de texto: ")
    resultado = cadena1 + " " +cadena2
    return resultado

def main():
    resultado_concatenacion = concatenar_cadenas()
    print("El resultado de concatenar las dos cadenas es:", resultado_concatenacion)

if __name__ == "__main__":
    main()



# 31 determinar si un numero es positivo, negativo o cero 


def determinar_signo(numero):
    if numero > 0:
        print("El número ingresado es positivo.")
    elif numero < 0:
        print("El número ingresado es negativo.")
    else:
        print("El número ingresado es cero.")

def main():
    try:
        numero = float(input("Ingrese un número: "))
        determinar_signo(numero)
    except ValueError:
        print("Error: Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()