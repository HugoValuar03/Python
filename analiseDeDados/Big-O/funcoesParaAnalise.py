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

print(n)
print(len(n))

# labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponencial']
# big_o = [np.ones(n.shape), np.log(n), n,n * np.log(n), n**2, n**3, 2**n]

plt.figure(figsize=(10,8))
plt.ylim(0, 100)
for i in range(len(big_o)):
    plt.plot(n, big_o[i], label = labels[i])
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')
plt.show()