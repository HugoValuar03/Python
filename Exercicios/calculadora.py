# Calculadora com while

while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite um número: ')
    operador = input('Digite o operador (+,-, *, /): ')

    numeros_validos = None #Ultilizando flags
    num1_float = 0
    num2_float = 0
    
    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True
    except Exception as error:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos os números são válidos')
        continue # Se o número for inválido, vai voltar para a parte de escrever o número
    
    operadores_permitidos = '+/-*'
    
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    
    ###
    if operador == '+':
        soma = num1_float + num2_float
        print(f'O resultado é {soma}')
    elif operador == '-':
        subtracao = num1_float - num2_float
        print(f'O resultado é {subtracao}')
    elif operador == '*':
        multiplicacao = num1_float * num2_float
        print(f'O resultado é {multiplicacao}')
    elif operador == '/':
        divisao = num1_float/num2_float
        print(f'O resultado é {divisao}')
    else:
        print('Como que chegou até aqui?')
    
    sair = input('Quer sair? [s]Sair: ').lower().startswith('s')

    if sair is True:
        break