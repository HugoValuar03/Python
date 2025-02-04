# Empacotamento e desempacotamento com args e kwargs

Caso haja dois dicionários como por exemplo:
```
pessoa = {
	'nome': 'Aline',
	'sobrenome': 'Souza',
}

dados_pessoa = {
	'idade': 16,
	'altura': 1.6,
}
```

Como faria para juntar esses dois dicionários?

Há algumas formas, por exemplo, criando um terceiro e "jogando" os dados de cada dicionário neste terceiro:

```
pessoa_completa = {**pessoa, **dados_pessoa} # Para extrair apenas os dados usa-se dois asteriscos
```

para imprimir esses dados, usaremos o \**kwargs:

```
def mosto_argumentos_nomeados(*args, **kwargs):
	print('NÃO NOMEADOS:', args)

	for chave, valor in kwargs.items():
		print(chave, valor)

mosto_argumentos_nomeados(1, 2, nome='Joana', qlq=123)
```

caso haja argumentos não nomeados nos argumentos da função, todos irão juntas para a parte 'NÃO NOMEADOS', como é mostrado no print acima.

A saída do código acima ficará da seguinte forma:

```
NÃO NOMEADOS: ()
nome Joana
qlq 123
```
