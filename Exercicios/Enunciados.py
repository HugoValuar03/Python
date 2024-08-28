"""
Faça um programa que peça ao usuário para digitar um número inteiro, 
informe se este número é par ou ímpar. Caso o usuário não digite um número 
inteiro, informe que não é um número inteiro.
"""
numero = input("Digite um número: ")
try:
    numero_int = int(numero)
    if (numero_int % 2 == 0):
        print("O número é par")
    else:
        print("O número é ímpar")
except:
    print("Não é um número inteiro")

"""
Faça um programa que pergunte a entrada ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input("Digite a entrada atual: ")
try:
    hora = int(entrada)
    if hora >= 0 | hora <= 11:
        print("Bom dia!")
    elif hora >= 12 | hora <= 17:
        print("Boa tarde!")
    elif hora >= 18 | hora <=23:
        print("Boa noite")
    else:
        print("Digite uma entrada válida")
except:
    print("Não é um número inteiro")
    
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; Maior que 6 escreva "Seu nome é muito grande".
"""

nome = input("Digite seu primeiro nome: ")
tamanho_nome = len(nome)
if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print("Seu nome é curto")
    elif (tamanho_nome >= 5 and tamanho_nome <= 6):
        print("Seu nome é normal")
    elif tamanho_nome > 6:
        print("Nossa, que nome grande você tem")
else:
    print("Você não digitou um nome")
