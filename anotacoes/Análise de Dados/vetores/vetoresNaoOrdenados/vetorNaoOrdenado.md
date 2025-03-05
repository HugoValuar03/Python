# Vetores não ordenados

Será utilizado a biblioteca numpy para a implementação dos vetores

````python
import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int) # O empty cria um vetor vazio, e ele define o tamanho a partir do valor passado na variável capacidade

    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print("posição:", i, ' -> ', self.valores[i])

vetor = VetorNaoOrdenado(5)
vetor.imprime()
````

Neste código, foi criado um vetor de tamanho 5, como foi passado pela linha de comando `vetor = VetorNaoOrdenado(5)`. Ao realizar a impressão em `vetor.imprime()`, retorna o texto "O vetor está vazio, pois ainda não foi adicionado nada"

````python
def insere(self, valor):
    if self.ultima_posicao == self.capacidade - 1:
        print('Capacidade máxima já foi atingida')
    else:
        self.ultima_posicao += 1
        self.valores[self.ultima_posicao] = valor
````

Aqui é adiciona a função de inserir valor, primeiramente verificando se o vetor não está cheio, se não estiver cheio, a variável `ultima_posicao` que inicia com valor −1, recebe +1, ficando assim com valor 0, que é o valor que os vetores iniciam, já que foi iniciado um vetor de 5 posições, as casas será 0, 1, 2, 3, 4. Para inserir um valor num vetor é feito o seguinte comando:

````doctest
vetor.insere(2)
vetor.insere(3)
vetor.insere(4)
vetor.insere(5)
vetor.imprime()
````

Após este comando, o valor que será retornado no terminal é:
````doctest
posição: 0  ->  2
posição: 1  ->  3
posição: 2  ->  4
posição: 3  ->  5
````
---
Agora para realizar uma pesquisa:
````python
def pesquisar(self, valor):
    for i in range(self.ultima_posicao + 1):
        if valor == self.valores:
            return i
        return -1
````