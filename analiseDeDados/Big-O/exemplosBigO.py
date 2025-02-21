# Constant - O(1): A execução só acontece uma vez

lista = [1,2,3,4,5]

def constant(n):
    print(n[0])

constant(lista)

# Linear - O(n): A quantidade de execuções depende do valor de n

def linear(n):
    for i in n:
        print(i)

linear(lista)

# Quadratic - O(n^2) - polynomial

def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)
        print('---')

quadratic(lista)

# Combination

def combination(n):
    # O(1)
    print(n[0])

    # O(5)
    for i in range(5):
        print('test', i)

    # O(n)
    for i in n:
        print(i)

    # O(n)
    for i in n:
        print(i)
    
    # O(3)
    print('Python')
    print('Python')
    print('Python')

combination(lista)