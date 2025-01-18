## Def
Palavra reservada usada p/ criar funções

### Ex.:

```
def escrever():
	print('Olá mundo')
```

$\rightarrow$ Há a  possibilidade de passar um argumento nomeado caso nenhum argumento seja inserido.
### Ex.:

```
def saudacao(nome='sem nome'):
	print(f'Olá, {nome}!')

saudacao('Luiz Otávio')
saudacao('Fernando')
saudacao()
	
```
```
saída:
	Olá, Luiz Otávio!
	Olá, Fernando!
	Olá, sem nome!
```
