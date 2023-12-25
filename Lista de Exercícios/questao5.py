#Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.   

numero1 = float(input("Digite um número:"))
numero2 = float(input("Digite outro número:"))
sinal = input("Digite um sinal:")

if sinal == '+':
    print(numero1 + numero2)
elif sinal == '-':
    print(numero1 - numero2)
elif sinal == '*':
    print(numero1 * numero2)
elif sinal == '/':
    print(numero1/numero2)
else:
    print("Reeinicie o programa e digite um sinal válido")
