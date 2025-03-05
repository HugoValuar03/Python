# Vetores ordenados

## Inserção
Será utilizada a mesma estrutura dos vetores não ordenados para inicialização e impressão de vetores:

````doctest
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
````
Para que os valores sejam impressos corretamente na ordem esperada, antes de tudo é feita uma verificação para verificar se a capacidade máxima foi atingida, utilizando o seguinte código:
````doctest
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
````
Se essa verificação for atendida, o valor não é inserido, caso contrário, seguirá para o próximo passo que é encontrar o local onde o valor terá que ser inserido:
````doctest
posicao = 0
for i in range(self.ultima_posicao + 1):
    posicao = i
    if self.valores[i] > valor:
        break
    if i == self.ultima_posicao:
        posicao = i + 1
````
Após encontrar o local, terá que ser refeito o remanejamento do vetor para encaixar o valor na ordem correta, e após o remanejamento será feita a inserção do valor:
````doctest
x = self.ultima_posicao
    while x >= posicao:
        self.valores[x+1] = self.valores[x]
        x -= 1

    self.valores[posicao] = valor
    self.ultima_posicao += 1
````
---
## Pesquisa

Para que a pesquisa seja feita de forma precisa, primeiro é feita uma pesquisa linear ao longo do vetor, para verificar se o valor é encontrado, se for encontrado retornará a posição que foi encontrado e o valor encontrado, caso contrário irá retornar 'Valor não encontrado':
````doctest
def pesquisar(self, valor):
    for i in range(self.ultima_posicao + 1):
        if self.valores[i] > valor:
            return print('Valor não encontrado')
        if self.valores[i] == valor:
            return print(f'Valor:', valor, ' encontrado na posição ', i)
        if i == self.ultima_posicao:
            return -1
````