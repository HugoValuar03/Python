# Dict
O `__dict__` ele retorna em forma de dicionário os dados do objeto.

Ex.:

```
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
p1 = Pessoa('João', 35)
print(p1.__dict__)
```

Saída:
```
{'nome': 'João', 'idade': 35}
```

O método `vars()` faz a mesma coisa

```
print(vars(p1))
```

A diferença é que o `__dict__` é editável, por exemplo, tem como adicionar, alterar e excluir dados, o `vars()` apenas exibe.