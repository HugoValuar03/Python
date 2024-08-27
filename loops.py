### Loops ###

# While

my_condicion = 0

while my_condicion < 10:
    print(my_condicion)
    my_condicion += 1
else: # É opcional
    print("A condição é maior que 10")    
    
print("A execução continua")

while my_condicion < 20:
    my_condicion += 1
    if(my_condicion == 15):
        print("para a execução")
        break
    
    print(my_condicion)

print()
print("Loop For")
print()
# For

my_list = [35, 24, 62, 52, 30, 30, 17]
    
for element in my_list:
    print(element)
    
print()
my_tuple = (35, 1.77, "Hugo", "Valuar", "Hugo")

for element in my_tuple:
    print(element)
    
print()
my_set = {"Hugo", "Valuar", 35}

for element in my_set:
    print(element)
    
print()
#Para imprimir as chaves
my_dict = {"Nome": "Hugo", "Sobrenome" : "Valuar", "Idade" : 19} 
for element in my_dict:
    print(element)
    
print()
#Para imprimir os valores de cada chave
my_dict = {"Nome": "Hugo", "Sobrenome" : "Valuar", "Idade" : 19} 
for element in list(my_dict.values()):
    print(element)