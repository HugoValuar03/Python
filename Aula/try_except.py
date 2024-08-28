"""
Introdução ao try/except
try -> tentar executar um código
except -> ocorreu erro ao executar
"""
numero_str = input('Vou dobrar o número que você digitar ')

try:
    print('STR',  numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'dobro de `{numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número')