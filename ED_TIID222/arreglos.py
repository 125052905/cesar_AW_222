""" #Declarando un arreglo
numeros = [10,20,30,40,50]

#Imprimimos un elemento espe. del arreglo
print(numeros[2])

#Reasignación
numeros[3] = 35
print(numeros)

#Agrega un nuevo valor al final del arreglo
numeros.append(60)
print(numeros)

#Eliminamos un valor en el arreglo
numeros.remove(35)
print(numeros)

#Eliminamos un valor del arreglo usando la posición
numeros.pop(4)
print(numeros)

frutas = ["Manzana", "Fresa", "Sandia", "Mango", "Melon", "Platano"]
frutas.pop(4)
print(frutas)


frutas.remove("Manzana")
print(frutas)

arreglo =[]

print(arreglo)



n = int(input("Ingrese el tamaño del arreglo"));

for i in range(n):
    dato = int(input("Ingrese un numero:"))
    arreglo.append(dato)
    print("El arreglo es:", arreglo)   """


numeros = []
for i in range(15):
    numero= int(input("Ingresa un numero:"))
    numeros.append(numero)
    cincuerizado = numeros.copy()
    for i in range (15):
        if cincuerizado[i] % 5 != 0:
            cincuerizado[i] = cincuerizado[i] + (5-cincuerizado[i]%5)

            print("\n Arreglo original")
            print(numeros)

            print("\n Arreglo cincuerizado")
            print(cincuerizado)

            

            
    

