# Closure

```
def criar_saudacao(saudacao, nome):
	return f'{sadudacao}, {nome}!'

saudacao1 = criar_saudacao('Bom dia', 'Luiz')
saudacao1 = criar_saudacao('Bom noite', 'Luiz')
print(saudacao1)
print(saudacao2)
```

O problema neste código em ter que criar um saudação para cada usuário, para isso temos a closure, que são funções dentro de funções

```
def criar_saudacao(saudacao, nome):
	def saudar():
		return f'{sadudacao}, {nome}!'
	return saudar

saudacao1 = criar_saudacao('Bom dia', 'Luiz')
saudacao1 = criar_saudacao('Bom noite', 'Luiz')

print(saudacao1())
print(saudacao2())
```

Ao retirar os parênteses do retorno da função, estou meio que obrigando o código a guardar os dados de saudacao1 e saudacao2 na memória, e ao imprimir, saudacao1 e 2 são passados como métodos.

Um exemplo prático de um uso que poderia ter seria o seguinte código:
```
def criar_saudacao(saudacao, nome):
	def saudar():
		return f'{sadudacao}, {nome}!'
	return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Bom noite')

for nome in ['Maria', 'Joana', 'Luiz']:
	print(falar_bom_dia(nome))

for nome in ['Fernando', 'Fábio', 'Joao']:
	print(falar_boa_noite(nome))
```

Saída:
```
Bom dia Maria!
Bom dia Joana!
Bom dia Luiz!
Bom noite Fernando!
Bom noite Fábio!
Bom noite Joao!
```