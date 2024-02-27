import math
def calcular_area_circulo (radio):
    area=math.pi*radio**2
    return area

def main ():
    try:
        radio= float (input("ingrese el radio del circulo: "))
        if radio <0:
            print("El radio no puede ser negativo")
        else:
            area = calcular_area_circulo (radio)
            print("El área del círculo con radio", radio, "es:", area)
    except ValueError:
        print("Error: Por favor ingrese un numero valido para el radio.")
if __name__== "__main__":
    main()


#17 
def concatenar_cadenas():
    cadena1= input("ingrese la primera cadena de texto:")
    cadena2= input("ingresa la segunda cadena de texto:")
    resultado = cadena1 + cadena2
    return resultado
def main():
    resultado_concatenacion =concatenar_cadenas()
    print("el resultado de concatenar las dos cadenas es:", resultado_concatenacion)
if __name__ == "__main__":
    main()
    

# 31
def determinar_signo (numero):
    if numero >0:
        print("El numero ingresado es positivo")
    elif numero <0:
        print("El numero ingresado es negativo")
    else:
        print("El numero ingresado es cero")
def main():
    try:
        numero = float(input("Ingrese un numero:"))
        determinar_signo (numero)
    except ValueError:
        print("Error: Por favor ingrese un numero valido.")
if __name__ == "__main__":
    main ()
    