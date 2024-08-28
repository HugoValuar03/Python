# É uma boa prática separar nomes de variáveis por "_".
my_variavel = "my variavel" 
print(my_variavel)

my_int_variavel = 3
print("Esta varivael e do tipo", type(my_int_variavel))

# Convertendo um número para String
my_int_to_str_varivel = str(my_int_variavel)
print(my_int_to_str_varivel)

# Concatenação de variáveis em um print
print("Esta variavel e do tipo" , type(my_int_to_str_varivel))

print(my_int_variavel) 
print(my_variavel, my_int_variavel)

# Algumas funções do sistema
# Função len()

nome = "Hugo"
print("O seu nome tem",len(nome), "caracteres") # Mostra quantos caracteres tem uma variável, String ou o que seja

# Variaveis em só uma linha (Não é uma boa prática, mas é possível)
nome, idade = "Hugo", 25
print("Ola", nome, "bem vindo, sua idade atual e de:", idade)

#Inputs
'''
nome = input("Qual seu nome? ")
cargo = input("Qual seu cargo? ")
print("Bem vindo", nome, "seu cargo é:", cargo)
'''

#Forçando o tipo
address: str = "Minha direção"
address: str = 32
print(type(address))


