# Enumerate - enumera iteráveis (índices)

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Jão')

# O enumerator enumera os itens da lista, e "consome" os itens, pois após realizar um for por exemplo, não é possível realizar outro, pois não há mais nada

for item in enumerate(lista):
    print(item)