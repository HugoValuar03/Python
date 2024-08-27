### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 1, 32, 44, 51]

print(my_list)
print(len(my_list))

my_other_list = [19, 177, "Hugo", "Valuar"]

print(type(my_other_list))
print(my_other_list)
print(len(my_other_list))

print()

print(my_other_list[-3])
print(my_other_list[-2])
print(my_other_list[-1]) #Mostra um item apartir do índice
print(my_other_list[-0])
print(my_other_list[0])
print(my_other_list[1]) 
print(my_other_list[2]) 
print(my_other_list[3]) 

print(my_other_list.count(19)) #Retorna quantas vezes o elemento passsado no 'count' se repete

age, heigh, name, last_name = my_other_list # Define as variaveis de acordo com a ordem das variaveis e ordem dos indices da lista
print(age)

print(my_other_list + my_list) # Une as duas listas

my_other_list.append("Awebo") #Adiciona um elemento na lista
print(my_other_list)

my_other_list.insert(1, "Fruta") #Insere um item apontando um indice específico
print(my_other_list)

my_other_list.remove("Fruta") #Remove um item da lista
print(my_other_list)

print(my_list)
print(my_list.pop()) # Imprime um item e logo após é removido
print(my_list)

print(my_list.pop(3)) # Imprime um item apartir do índice e logo após é removido
print(my_list)

del my_list[2] # Apenas deleta um elemento da lista apartir do índice
print(my_list)

'''

A diferença do .remove() para o del

O .remove() remove apartir do item passado
Ex: my_list.remove(24)

O del remove apartir do índice
Ex: del my_list[3]

'''
print()

my_new_list = my_list.copy() # Cria uma cópia da lista passada com o método
print(my_list)
print(my_new_list)

print(my_new_list.reverse()) #Inverte a lista
print(my_new_list)

print(my_new_list.sort()) #Ordena a lista em forma crescente
print(my_new_list)