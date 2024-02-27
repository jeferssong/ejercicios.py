def main():
    
    dias_semana = {
        1: "lunes",
        2: "martes",
        3: "miércoles",
        4: "jueves",
        5: "viernes",
        6: "sábado",
        7: "domingo"
    }

   
    numero = int(input("Ingrese un número del 1 al 7: "))


    if numero < 1 or numero > 7:
        print("Número fuera de rango. Por favor, ingrese un número del 1 al 7.")
    else:
        
        dia = dias_semana[numero]
        print("El día correspondiente al número {} es: {}".format(numero, dia))

if __name__ == "__main__":
    main()



    for i in range(1, 121):
    
     if i % 2 == 0:
        
        print(i)





        for i in range(1, 61):
            cuadrado = i ** 2
    
    print("El cuadrado de", i, "es", cuadrado)








numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))


print("Suma:", numero1 + numero2)
print("Resta:", numero1 - numero2)
print("Multiplicación:", numero1 * numero2)


if numero2 != 0:
    print("División:", numero1 / numero2)
else:
    print("División: No se puede dividir por cero")

print("Potencia:", numero1 ** numero2)