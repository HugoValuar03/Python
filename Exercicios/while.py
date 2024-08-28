nome = 'Hugo Valuar'
tamanho_nome = len(nome)

print(nome)
print(tamanho_nome)

contador = 0
novo_nome = ''
while contador < tamanho_nome:
    letra = nome[contador] + '*'
    novo_nome += letra
    print(f'*{novo_nome}')
    contador += 1