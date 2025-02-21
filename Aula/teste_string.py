"""
Execício
Peça ao usuário para digitar o seu nome
Peça ao usuário para digitar a sua idade
Se nome e idade forem digitados:
    Exiba:
        O seu nome é {nome}
        O seu nome invertido é {nome invertido}
        O seu nome contém (ou não) contém espaços
        O seu nome tem {quantidade de letras} letras
        A primeira letra do seu nome é {letra}
        a última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if not idade.isspace() and not nome.isspace:
    if idade.isdigit():
        print(f"Seu nome é {nome}")
        print(f"Seu nome invertido é {nome[::-1]}")
        if ' ' in nome or ' ' in idade:
            print("Tem espaços no seu nome")
        else:
            print("Não tem espaços no seu nome")
        print(f"Seu nome tem {len(nome)} letras")
        print(f"A primeira letra do seu nome é {nome[0]}")
        print(f"A ultima letra do seu nome é {nome[-1]}")
    else:
        print("Você digitou um número inválido")
else:
    print("Você deixou espaços em branco")