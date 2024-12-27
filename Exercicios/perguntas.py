perguntas = [
    {
        'pergunta': 'Quanto é 2+2?',
        'opcoes': ['1', '2', '3', '4', '5'],
        'resposta': '4',
    },
    {
        'pergunta': 'Quanto é 5*5?',
        'opcoes': ['25', '55', '10', '51'],
        'resposta': '25',
    },
    {
        'pergunta': 'Quanto é 10/2?',
        'opcoes': ['2', '5', '1', '3'],
        'resposta': '5',
    }
]

contador_acertos = 0

for pergunta in perguntas:
    
    print('pergunta',pergunta['pergunta'])
    print()
    
    for i, opcao in enumerate(pergunta['opcoes']):
        print(f'{i+1})',opcao)    
    print()
    
    escolha = input('escolha uma opção: ')
    
    print()
    
    if escolha == pergunta['resposta']:
        contador_acertos = contador_acertos + 1
        print('Resposta correta ✅')
    else:
        print('Resposta errada ❌')
        
print(f'Você acertou {contador_acertos} de 3 perguntas')