"""
Interpolação básica de strings
=====================================
s - string
d e i - int
f - float
x e X - Hexadecimal (BDA31C)
"""
nome = 'Hugo'
preco = 1000.29123123
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)