"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    # Definição
    print(x + y + z)
    
soma(1, 2, 3) # Argumento não nomeado
soma(y=1, z=3, x=2) # Argumento nomeado
print(1, 2, 3, sep='-') 