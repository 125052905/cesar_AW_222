numeros =[10,20,30,40]
numeros.insert(2,95)
numeros.extend([50,67])
print("Arreglo completo:",numeros)
print("Numero 95:",numeros[2])
print("Numero 67:",numeros[6])
print("El número 95 ocupa la posición:", numeros.index(95))
print("El número 67 ocupa la posición:", numeros.index(67))
