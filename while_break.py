"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""

# condicao = True

# while condicao:
#     nome = input('Qual seu nome?: ')
#     if nome == 'sair':
#         print('Volte sempre')
#         break # Busca o while mais próximo dele
#     print(f'Seu nome é {nome}')
   
    
qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha} {coluna}')
        coluna += 1
    linha +=1

