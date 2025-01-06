# Dicionários

Para criar um dicionário usamos ==dict== ou =={ }==

```
pessoa = {}

print(pessoa, type(pessoa))
```

Saída: `{} <class 'dict'>`

Para criar um dicionário, fica mais fácil organizar semelhante ao formato JSON

Ex.:
```
pessoa = {
	'nome': 'Luiz Otávio',
	'sobrenome' : 'Ferreira',
	'idade': 18,
	'altura': 1.8
}

print(pessoa, type(pessoa))
```

Saída: `{'nome': 'Luiz Otávio', 'sobrenome' : 'Ferreira'} <class 'dict'>`

Outro exemplo para criar um dicionário seria usando o dict()

```
pessoa = dict(nome='Luiz Otávio', sobrenome='Ferreira')
```

'nome' é a chave, e 'Luiz Otávio' é o dado que a chave nome contém

Porém não é muito usado esta forma, então é mais indicado criar com as chaves

----

Para acessar um valor de um dicionário é da seguinte forma:

```
print(pessoa['nome'])
```

Ao realizar o `print()`, passa-se o nome do dicionário, e entre colchetes coloca a chave entre aspas simples

---
### Acessar itens

Para retornar todas as chaves faça-se da seguinte forma:
```
for chave in pessoa:
	print(chave)
```

agora para imprimir tanto a chave quanto o dado de cada chave de forma organizada, faça-se da seguinte forma:
```
for chave in pessoa:
	print(chave, pessoa[chave])
```

Caso queira imprimir apenas os dados da chave, basta tirar `chave` do `print()`, deixando apenas `pessoa[chave]`
___
### Resumindo

Em resumo, dicionários são usados para qualquer coisa que tenha mais de um atributo, por exemplo, pessoa tem nome, sobrenome, idade, altura e etc.

___
### Alterar valor

Para alterar o valor da chave, basta sobrescrever com outro valor

---
### Deletar

Para deletar uma chave

```
del pessoa['sobrenome']
```

___
## Métodos úteis para dicionários

### Métodos dunder

*Os exemplos a seguir serão apartir do seguinte código:*
```
pessoa = {
	'nome': 'Luiz Otávio'
	'sobrenome': 'Miranda'
}
```
### \__ len__

Neste exemplo retorna a quantidade de chaves que eu tenho no dicionário

```
print(pessoa.__len__())
```
Saída:`2`

porém é a mesma coisa que
```
print(len(pessoa))
```

#### keys()

Retorna todas as chaves do dicionário

```
print(list(pessoa.keys()))
```

Saída: `['nome', 'sobrenome']`

Em um laço for ficaria:
```
for chaves in pessoa.keys():
	print(chaves)
```
#### values()

Retorna todos os valores do dicionário
```
print(list(pessoa.values()))
```

Saída:`['Luiz Otávio', 'Miranda']`

Em um laço for ficaria:
```
for valor in pessoa.values():
	print(valor)
```

#### items()

Retorna a chave e o valor 
```
print(list(pessoa.items()))
```

Saída:``[('nome', 'Luiz Otávio'), ('sobrenome', 'Miranda')]`

Em um laço for ficaria:
```
for chave, valor in pessoa.values():
	print(chave valor)
```
#### update()

Atualiza o dicionário
```
p1.update({
	'nome': 'novo valor', # Atualiza a chave nome
	'idade': 30, # Cria chave idade já passando um valor
})

print(p1)
```

Também pode ser escrito da seguinte forma:
```
p1.update(nome='novo valor', idade=30)
```
### Shallow Copy e Deep Copy

```
d1 = {
	'c1': 1,
	'c2': 2,
}
```

#### Shallow Copy (Cópia rasa)

Significa *cópia rasa* 

d2 = d1.copy()

A partir desta cópia, tudo que estiver no dicionário d1, irá para o dicionário d2, e se algo for alterado no dicionário d2, não será alterado no d1. 

#### Deep copy (Cópia profunda)

Porém caso houver dentro de uma lista dentro do dicionário como por exemplo:

```
d1 = {
	'c1': 1,
	'c2': 2,
	'l1': [0, 1, 2]
}
```

Será preciso fazer um deep copy.

Para fazer isso, é preciso importar o módulo copy

```
import copy
```

A seguir, para fazer o deep copy, é preciso importar do módulo copy

```
d2 = copy.deepcopy(d1)
```

Agora irá copiar tudo

#### get()

Retorna o valor da chave especificada

```
print(d1.get('nome'))
```

#### pop()

Apaga a chave porém retorna a chave excluída, é como se fosse o del, mas o pop retorna o item excluído

```
print(d1.pop('nome'))
```

#### popitem()

Apaga a última chave do dicionário
```
print(d1.popitem())
```
