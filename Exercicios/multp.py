def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def par_impar(numero):
    if numero % 2 ==0:
        return 'Seu número é par'
    return 'Seu número é impar'
        
print(multiplicar(1, 2, 3))
print(par_impar(12314112412412412412313131237))

