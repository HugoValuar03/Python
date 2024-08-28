# While/else
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    print(letra)
    i += 1
else:
    print('O else foi executado') #Executa se o while for inteiramente concluído
print('Fora do while')