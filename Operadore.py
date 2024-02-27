#Operadores Arimeicos 

numero1 = 77
numero2 = 44  # operador asignacion =

resta= numero1 - numero2
suma = numero1 + numero2
multiplicacion = numero1 *numero2
division = numero1 / numero2
resto= numero1 % numero2

print("******CALCULADORA******")
print(F"LA RESTA ES: {resta}")
print(f"LA SUMA ES:{numero1 + numero2}")
print(f"LA MULTIPLICLACION ES: {numero1 * numero2}")
print(f"LA DIVICION ES: {numero1 / numero2}")
print(f"EL RESIDUO DE LA DIVISION ES:", resto)

#Operadores de asignacion 
edad= 55
print(edad)


edad +=5  #sumarle 5 a lo que ya tiene
edad= edad + 5

edad -=5
print(edad)

#ENTRADA
nombre = input("Cual es tu nombre?:  ")
edad = input("Cual es tu edad?:  ")

#salidad
print("Me alegro de concerte, bienbenido",nombre, "veo que tienes", edad, "años !!" )
print("Me alegro de conocerte, bienvenido",nombre, "veo que en el 2023 tendras", int(edad)+2, "años !!")

#Condicionales 

#ejemplo1
print("###################EJEMPLO1##############")

color ="rojo"

if color == "rojo":
    print("El color es ROJO")
else:
    print("El color no es ROJO")

#Ejemplo2
print("###################EJEMPLO2##############")

color = input("Adivina cual es mi color favorito:   ")

if color == "rojo":
    print("El color es ROJO")
else:
    print("El color incorrecto!!")

#Eejemplo1
#condicion si el año ingresado es esa variable es mayor o menor 
    
print("###################EJEMPLO 1##############")

year = 2020

if year == 2021:
    print("Estamos del 2021 en adelnate")
else:
    print("Es un año anterior al 2021")

#Ejemplo2
    
print("###################EJEMPLO 2 ##############")

year = int(input("¿En que año estanos:    "))

if year >= 2021:
    print("Estamos el 2021 en adelnate")
else:
    print("Es un año anterior al 2021")
