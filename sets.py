### Sets ###

my_set = set()
my_other_set = {}

print(type(my_other_set)) # Inicialmente é um dicionario
 
my_other_set = {"Hugo", "Valuar", 19}

print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Bailona")
print(my_other_set) # Um set não é uma estrutura ordenada

my_other_set.add("Bailona") # Um set não admite valores repetidos
print(my_other_set)

#Verificar se existe
print("Valuar" in my_other_set) 
print("Valaur" in my_other_set)

my_other_set.remove("Valuar")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set