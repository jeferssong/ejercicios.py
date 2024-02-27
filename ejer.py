pais = "Marruecos"
continente = "Asia"
year = 2023
print(f"{pais} - {continente} - {str(year)}")


#ejercicio 2
contador = 1
for contador in range(1,121):
    if contador%2 ==0:
        print(contador)






#ejercicio 3
contador = 0
while contador <= 60:
    cuadrado = contador*contador
    print(f"El cuadro de {contador} es {cuadrado}")

    contador += 1
              





#ejercicio 4
 
    numero1 = int(input("Introduce un primer numero:"))
    numero2 = int(input("Introduce el segundo numero:"))

    print("#### CALCULADORA ####")
    print("Suma: " + str (numero1+numero2))
    print("Resta:" + str (numero1-numero2))
    print("Multiplicacion:" + str (numero1*numero2))
    print("Divicion:" + str(numero1/numero2))








    #ejercicio 5

numero1 = int(input("introduce el primer numero: "))
numero2 = int(input("introduce el segundo numero:"))
if numero1 < numero2:

    for contador in range (numero1, (numero2 + 1)):
        print(contador)
else:
    print("El numero 1 debe ser menor al numero 2")






    #ejercicio 6

    for cabecera in range (1, 11):
        print("##########################")
        print(f"###### Tabla del {cabecera} ######")
        print("##########################")

        for numero in range (1, 11):
            print(f"{numero} x {cabecera} = {numero*cabecera}")

            print("\n")




# ejercicio 7 


numero1 = int (input("introduce un numero:"))
numero2 = int (input("introduce el siguiente numero: "))

if numero1 < numero2:
    for x in range (numero1, (numero2 + 1)):

        if x%2 == 0:
            print(f"{x} es PAR")
        else:
            print(f"{x} es IMPAR")
else:
    print("El numero 1 debe ser mayor al 2")


    

    #ejercicio 8

    numero = int(input("introduce el numero: "))
    porcentaje = int(input(f"¿ Que porcentaje quieres sacar de {numero}?"))

    operacion = (numero * (porcentaje/100))
    print(f"El {porcentaje}% de {numero} es: {operacion}")




    #ejercicio 9



    contador = 1 
    while contador < 100:
        numero = int(input("Introduce un numero: "))
         
        if numero == 111:
            break
        else:
            print(f"Has introducido el: {numero}")






#ejercicio 10
            




contador=1
aprobados=0
reprobados=0


numero_alumnos=int (input("cuantos aprendicies tienes?:"))

while contador <= numero_alumnos:
    nota= int(input(f" Que nota quieres ponerle al aprendiz {contador}?: "))
    if nota >= 3:
        aprobados +=1
    else:
        reprobados +=1
    
    contador +=1

print(f"Aprendices Aprobados: {aprobados}")
print(f"Aprendices Reprobados: {reprobados}")



#ejercicio 11 




nombre = "tony soprano"
edad =  int ("51")








# ejercicio 12
nombre = "julia"
apellido = "Roberts"
nombre_completo = "julia Roberts"
