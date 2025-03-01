import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1 # Aqui é definido um ponteiro para saber se o vetor está ou não vazio, e para saber quantos espaços do vetor foram ocupados
        self.valores = np.empty(self.capacidade, dtype=int) # O empty cria um vetor vazio, e ele define o tamanho a partir do valor passado na variável capacidade

    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print("posição:", i, ' -> ', self.valores[i])

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima já foi atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return print(i)
            return -1

    def excluir(self, valor):
        posicao = self.pesquisar(valor) # Pega o local que o valor está, e ao invés de fazer uma pesquisa linear, o metodo vai direto para a posicao
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= -1

vetor = VetorNaoOrdenado(5)
vetor.imprime()

vetor.insere(2)
vetor.insere(3)
vetor.insere(4)
vetor.insere(5)
vetor.insere(8)
vetor.imprime()

vetor.pesquisar(10)

vetor.excluir(3)
print()
vetor.imprime()