minha_lista = ["Abacaxi", "Melancia", "Abacate"] #lista de Strings
minha_lista2 = [1,2,3,4,5] #lista de inteiros
minha_lista3 = ["Abacaxi", 2, "Frango", 3.0] #lista mista

print(minha_lista) #imprimir lista
print(minha_lista2) #imprimir lista 
print(minha_lista3) #imprimir lista

print()

print(minha_lista[2]) #imprimir por índice

print()

tamanho = len(minha_lista) #Define o tamanho da lista
print(tamanho) #Imprime o tamanho da lista

print()

minha_lista.append("limao")
print(minha_lista) #Adiciona um novo item

if 3 in minha_lista2:
    print("3 está na lista")

print()

del minha_lista[2:] #Apagou do índice 2 pra frente 
print(minha_lista) 

print()

minha_lista4 = []

minha_lista4.append(57)
print(minha_lista4)

print()

lista = [14,2141,412,41,241,241,5124,12,41,241,24,123,12,4,141,24]

lista.sort() #Ordena a lista numéricamente, ordena uma lista que já existe
print(lista)

lista = sorted(lista) #Retorna uma lista já ordenada
print(lista)

lista.sort(reverse=True) #Ordena a lista em ordem decrescente 
print(lista)
lista.reverse #Inverte a lista (ultimo é o primeiro, penultimo é o segundo, e assim por diante)
print(lista)
