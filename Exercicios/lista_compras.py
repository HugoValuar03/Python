"""
Faça uma lista de compras com listas
O usuário dever ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista
"""

print('Bem vindo a lista de compras!')
lista_compras = []

while True:
    print('1 - Inserir item')
    print('2 - Alterar item')
    print('3 - Listar')
    print('4 - Sair')
    opcao = input('Digite um a opção: ')
    print()

    match(opcao):
        case '1':
            item_add = input('Digite o nome do item: ')
            lista_compras.append(item_add)
            print()
            continue
        
        case '2':
            for itens in lista_compras:
                print(itens)
            print()
            item_alter = input('Digite o item para alterar: ')
            if item_alter in lista_compras:
                lista_compras[lista_compras.index(item_alter)] = input('Digite o novo item: ')
            else: 
                print('Item não encontrado')
            print()
            continue

        case '3':
            if len(lista_compras) >= 1:
                for itens in lista_compras:
                    print(f'-> {itens}')
            else:
                print('Lista vazia')
                print()
                continue
            print()
        case '4':
            print('Obrigado por usar')
            break
        
        case _:
            print('Digite uma opção válida')
            print()
            continue
