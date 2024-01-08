x = [1, 2, 3, 4, 5]
y = []

print("Usando a forma normal")
for i in x: 
    y.append(i ** 2)
    
print(x)
print(y)

print()
print("Usando list_comprehension")
a = [1, 2, 3, 4, 5] 
b = [i ** 2 for i in a] #imprimir todos os itens da lista
z = [i for i in x if i%2 == 1] #imprime os número ímpares

print(a)
print(b)
print(z)