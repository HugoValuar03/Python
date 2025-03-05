import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores =np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return

        # Encontrar a posição que será realizada a inserção
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        # Remanejar os valores, colocando os valores maiores que o encontrado vão para a próxima posição a frente para poder incluir o novo valor
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x+1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    # Pesquisa linear
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return print('Valor não encontrado')
            if self.valores[i] == valor:
                return print(f'Valor:', valor, ' encontrado na posição ', i)
            if i == self.ultima_posicao:
                return -1

vetor = VetorOrdenado(10)
vetor.imprime()

vetor.insere(9)
vetor.insere(6)
vetor.insere(7)
vetor.insere(5)
vetor.insere(2)
vetor.insere(4)
vetor.imprime()

vetor.pesquisar(9)
