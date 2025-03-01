# Notação Big-O

- Comparar dois algoritmos
- Comparação objetiva entre dois algoritmos
- Considera diferenças entre poder de processamento, sistema operacional, e linguagem de programação
- O quanto a "complexidade" do algoritmo aumenta de acordo com as entradas

## Exemplo:

```
def soma1(n):
    soma = 0
    for i in range(n+1):
        soma += 1
    return soma
```

Executando em seguida o `%timeit soma2()`, retorna que o tempo médio de execução é de $116ns$, sendo 6 vezes mais rápido de rodar que o anterior, obtendo o mesmo resultado.

# Notação Big-O em lista

Na seguinte lista, o objetivo é listar todos os números de 1 a 1000

```
def lista2():
    return range (1000)
    
l = lista2()

for i in l:
    print(i)
```

Realizando o `%timeit`, retorna um tempo de `270ns`

---
# Funções para análise de dados

```
from math import log
import numpy as np
import matplotlib.pyplot as plt

# 1 Constant: np.ones(n.shape)
# log(n) Logarithmic: np.log(n)
# n Linear: n
# nlog(n) Log Linear: n * np.log(n)
# n^2 Quadratic: n**2
# n^3 Cubic: n**3
# 2^n Exponencial: 2**n

n = np.linspace(1, 10, 100) # Irá gerar 100 números entre 1 e 10
# print(n)

Saída:

[ 1.          1.09090909  1.18181818  1.27272727  1.36363636  1.45454545
  1.54545455  1.63636364  1.72727273  1.81818182  1.90909091  2.
  2.09090909  2.18181818  2.27272727  2.36363636  2.45454545  2.54545455
  2.63636364  2.72727273  2.81818182  2.90909091  3.          3.09090909
  3.18181818  3.27272727  3.36363636  3.45454545  3.54545455  3.63636364
  3.72727273  3.81818182  3.90909091  4.          4.09090909  4.18181818
  4.27272727  4.36363636  4.45454545  4.54545455  4.63636364  4.72727273
  4.81818182  4.90909091  5.          5.09090909  5.18181818  5.27272727
  5.36363636  5.45454545  5.54545455  5.63636364  5.72727273  5.81818182
  5.90909091  6.          6.09090909  6.18181818  6.27272727  6.36363636
  6.45454545  6.54545455  6.63636364  6.72727273  6.81818182  6.90909091
  1.          7.09090909  7.18181818  7.27272727  7.36363636  7.45454545
  7.54545455  7.63636364  7.72727273  7.81818182  7.90909091  8.
  8.09090909  8.18181818  8.27272727  8.36363636  8.45454545  8.54545455
  8.63636364  8.72727273  8.81818182  8.90909091  9.          9.09090909
  9.18181818  9.27272727  9.36363636  9.45454545  9.54545455  9.63636364
  9.72727273  9.81818182  9.90909091 10.        ]

labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponencial']

big_o = [np.ones(n.shape), n.log(n), n,n * np.log(n), n**2, n**3, 2**n]

  

plt.figure(figsize=(10,8))
plt.ylim(0, 100)
for i in range(len(big_o)):
    plt.plot(n, big_o[i], label = labels[i])
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')
plt.show()
```

![img.png](../assets/img.png)
