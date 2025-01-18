# Classes

* Classes são moldes para criar novos objetos (instâncias) que podem ter seus próprios atributos e métodos
* Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações
* Por convenção, usamos PascalCase para nomes de classes

<br>

Para criação de uma classe é da seguinte forma:
```
    class Pessoa:
        ...

    p1 = Pessoa()
    p1.nome = 'Luiz'
    p1.sobrenome = 'Otávio'

    print(p1.nome)
    print(p1.sobrenome)
```

Neste código está inicializando um objeto, porém para criar cada pessoa, teria que instânciar `p1.nome = 'nome'` e a mesma coisa para sobrenome, para agilizar este processo, utilizaremos o `__init__`

    ```
    class Pessoa:
        def __init__(self, nome, sobrenome):
            self.nome = nome
            self.sobrenome = sobrenome

    p1 = Pessoa('Luiz', 'Otávio')
    p2 = Pessoa('Maria', 'Joana')
    ```

## Métodos
Será utilizado este código como base:
```
class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()
```
Saída:
```
Fusca
Fusca está acelerando...
Celta
Celta está acelerando...
```

Um método é uma função que está dentro da classe e usa o primeiro parâmetro tem que ser `self`

## Atributos de Classe

```
Class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        reuturn ANO_ATUAL - self.idade

p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(p1.get_ano_nascimento)
print(p2.get_ano_nascimento)
```