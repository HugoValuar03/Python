"""
split e join com list e str
split - divide uma string (retorna uma lista)
join - juntar uma lista de strings
"""

frase = 'Olha só, que coisa interessante'

lista_frases = frase.split(',') # A frase vai quebrar no caracter indicado 

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip())

# strip() -> Apaga os espaços pra frente e pra trás 
# rstripe() -> Apaga os espaços a direita
# lstrip() -> Apaga os espaços a esquerda
print(lista_frases)

frase_unidas = ','.join(lista_frases)
print(frase_unidas)