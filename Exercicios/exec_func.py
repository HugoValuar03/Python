def multiplicar(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

multiplicacao = multiplicar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def par_impar(numero):
    multiplo = numero % 2 == 0
    if multiplo:
        return print('f{numero} é par')
    return 'f{numero} é impar'
    
print(multiplicacao)
print(par_impar(8))