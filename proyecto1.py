# Solicitar al usuario que ingrese dos palabras
palabra1 = input("Ingresa una palabra que describa tu cerveza: ")
palabra2 = input("Ingresa otra palabra que describa tu cerveza: ")

# Combinar las palabras para formar el nombre de la cerveza
nombre_cerveza = palabra1.capitalize() + " " + palabra2.capitalize()

# Imprimir el nombre de la cerveza
print("El nombre de tu cerveza es:", nombre_cerveza)