### Lists ###

my_list = list() # Uma forma de criar uma lista
my_other_list = [] # Outra forma de criar uma lista

print('imprimindo o tamanho da lista recém criada: ') 
print(len(my_list)) # Imprime o tamanho da lista
my_list = [35, 24, 1, 32, 44, 51] # Adicionando elementos na lista

print()
print('Re-imprimindo a lista com os valores aplicados')
print(my_list) # 
print(len(my_list)) # pegando o tamanho da lista

my_other_list = [19, 177, "Hugo", "Valuar"] 

print(type(my_other_list)) # Pegando o tipo da lista
print(my_other_list) # Imprimindo a lista
print(len(my_other_list)) # Imprimindo o tamanho da lista

print()

### Mostra um item apartir do índice ###
print(my_other_list[-3])
print(my_other_list[-2])
print(my_other_list[-1]) 
print(my_other_list[-0])
print(my_other_list[0])
print(my_other_list[1]) 
print(my_other_list[2]) 
print(my_other_list[3]) 

print(my_other_list.count(19)) #Retorna quantas vezes o elemento passsado no 'count' se repete

# Desempacotamento
age, heigh, name, last_name = my_other_list # Define as variaveis de acordo com a ordem das variaveis e ordem dos indices da lista

# Desempacotamento em chamadas de funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# p, b, *_, ap, u = lista
# print(p, u) # Resultado: Maria 

print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print(*lista) #Retorna a mesma coisa do print acima

# Necessita ter o mesmo número de variáveis para o mesmo número de itens na lista
print(age)

print(my_other_list + my_list) # Une as duas listas

my_other_list.append("Awebo") #Adiciona um elemento na lista
print(my_other_list)

my_other_list.insert(1, "Fruta") #Insere um item apontando um indice específico
print(my_other_list)

my_other_list.remove("Fruta") #Remove um item da lista
print(my_other_list)

print(my_list)
print(my_list.pop()) # Remove o ultimo ítem com índice mais alto, e retorna o item removido
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
Ao remover, o python reorganiza os índices da lista
'''
print()

my_new_list = my_list.copy() # Cria uma cópia da lista passada com o método
print(my_list)
print(my_new_list)

'''
Se voce faz por exemplo:
lista_a = ['Luiz', 'Maria]
lista_b = lista_a
Você não está copiando uma lista, você está fazendo duas variáveis 
apontarem para um mesmo valor na memória
'''

print(my_new_list.reverse()) #Inverte a lista
print(my_new_list)

print(my_new_list.sort()) #Ordena a lista em forma crescente
print(my_new_list)

list_c = my_list + my_other_list
print(list_c) # Une as duas listas
