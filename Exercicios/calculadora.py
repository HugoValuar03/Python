# Calculadora com while

numero1 = input('Digite um valor para realizar uma soma ')
numero2 = input('Digite outro valor ')

if numero1.isdigit() and numero2.isdigit():
    numero1 = int(numero1)
    numero2 = int(numero2)
    while True:
        soma = numero1 + numero2
        print(f'O resultado da soma é {soma}')
        
        sair = input('Deseja sair? [s]sim ')
        sair = sair.lower()
        if sair == 's':
            print('Obrigado por usar')
        break

