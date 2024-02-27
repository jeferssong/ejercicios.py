contador = 0

for contador in range(0,5):
    print("Voy por el " +str(contador))


#ejemplo mostrando los numeros de 1 a 100
    contador =1
    while contador<=100:
        print(f"Estoy en el numero:{contador}")
        contador = contador +1

        print("##### Ejemplo #####")
        numero_usuario =int(input("De que numero quieres la tabla?"))
        if numero_usuario<1:
            numero_usuario =1
    print(f"### Tabla del {numero_usuario}###")
    contador =1        
    while contador <=-10:
        print(f"{numero_usuario} x {contador} = {numero_usuario * contador }")
        contador += 1

    else:
        print("tabla terminada.")
