# Valores padrão

$\rightarrow$ Ao definir uma função, os parâmetros podem ter valores padrão. Caso não seja enviado para o parâmetro, o valor padrão será usado.

```
def soma(x, y, z=0):
	if z:
		print(f'{x=} {y=} {z=}', x + y + z)
	else: 
		print(f'{x=} {y=}', x + y)
```

Caso a função acima seja feita, se passar um valor zero para o z, como por exemplo:

```
soma(300, 200, 0)
```

A saída seria:
```
x=300 y=200 500
```

para resolver tal assunto, é usado o `is not None`, e passando um valor nulo para z, como no seguinte exemplo:
```
def soma(x, y, z=None):
	if z is not None:
		print(f'{x=} {y=} {z=}, x + y + z)
	else:
		print(f'{x=} {y=}, x + z)
```

Nesse caso a saída seria:
```
x=300 y=200 z=0 500
```

Como era esperado desde o início.

## Observação

Quando se passa um valor padrão em um parâmetro, todos os parâmetros que vierem após o parâmetro nomeado, tem que ser nomeado também

Exemplo que não pode acontecer:
```
def soma(x, y=None, z):
	...
```

Exemplo do correto:

```
def soma(x, y, z=None, a=None, b= None):
	...
```
