### Exception Handlign ###

n1 = 5
n2 = 1
n2 = "1"

#try except

try:
    print(n1 + n2)
    print("Não houve erro")
except:
    print("Não é possível somar")

# try except else

try:
    print(n1 + n2)
    print("Não houve erro")
except:
    print("Não é possível somar")
else:
    # Só executa se não produz um exception
    print("A execução continua corretamente")
    
# try except else finally
    
try:
    print(n1 + n2)
    print("Não houve erro")
except:
    print("Não é possível somar")
else: # Opcional
    # Só executa se não produz um exception
    print("A execução continua corretamente")
finally: # Opcional
    # Executa sempre, independente do resultado acima
    print("A execução continua")
    
# Exceptions por tipo

try:
    print(n1 + n2)
    print("Não foi produzido um erro")
except ValueError:
    print("Foi produzido um ValueError")
except TypeError:
    print("Foi produzido um TypeError")

# Captura de informação da exception

try:
    print(n1 + n2)
    print("Não foi produzido um erro")
except ValueError as error:
    print(error)