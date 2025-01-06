args seria argumentos não nomeados

\*args (empacotamento e desempacotamento), é chamado de args por convenção

um exemplo de desmpacotamento seria:
```
x, y, *resto = 1, 2, 3, 4
print(x, y, *resto)
```

o \*resto seria do 3 pra frente 

## Empacotamento

Se for escrito o seguinte código:
```
def soma(*args)
	print(args)

soma(1, 2, 3, 4, 5, 6)
```

será exibido o seguinte retorno:

```
(1, 2, 3, 4, 5, 6)
```

Está entre parêntese por ser uma tupla

Para o código:
```
def soma(*args)
	total = 0
	for numero in args:
		total += numero
	return total

soma(1, 2, 3, 4, 5, 6)
```
a saída será: ``21``
## Desempacotamento

Um exemplo de desempacotamento seria
```
def soma(*args)
	total = 0
	for numero in args:
		total += numero
	return total

numeros = 1, 2, 3, 4, 5, 12, 14, 51
soma_aleatoria = soma(*numeros)
```

Se realizer os seguintes prints
```
print(*numeros)
```
Saída: ``1, 2, 3, 4, 5, 12, 14, 51``

```
print(soma_aleatoria)
```
Saída: ``116``

Se for usado a função ``sum()``, o resultado será:

```
print(sum(numeros))
```
Saída: ``116``
