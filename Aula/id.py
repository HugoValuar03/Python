"""
Flag (Bandeira) - Marcar um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

v1 = 'a'
v2 = 'b'
print(id(v1)) # Resultado: 140735293525216
print(id(v2)) # Resultado: 140735293526272

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True #Não é legal de se fazer
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)