# Retorno

Ao contrário do print que exibe algo na tela, o return ele apenas "pega" esse valor
## Exemplo.:
```
def soma(x, y):
	return x + y
```

Só pode ter um return por função, caso houver o seguinte código:
```
def soma(x,y):
	if x>10:
		return 10
	return x + y
```

Só vai retornar $x+y$  se $x>10$ for falso