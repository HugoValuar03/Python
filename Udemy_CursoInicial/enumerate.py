lista = ["abacate", "bola", "cachorro"]

print("Modo normal")
for i in lista:
    print(i)
    
print("Usando a função enumarate")
for i, nome in enumerate(lista):
    print(i, nome)