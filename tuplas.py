### Tuplas ###

my_tuple = tuple()
my_other_tuple = () # Se tiver colchete é lista, se tiver parêntese é tupla

my_tuple = (35, 1.77, "Hugo", "Valuar")
my_other_tuple = (35, 60, 30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count(35))
print(my_tuple.index("Valuar"))

#my_tuple[1] = 1.80 --> 'tuple' object does not support item assignment
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

#Por definição, a diferença entre Lista e Tupla, é que a Tupla é imutável

my_tuple = list(my_tuple) #Transformando a tupla em lista
print(type(my_tuple))

my_tuple[2] = "Bailona"
my_tuple.insert(1,"Vermelho")
my_tuple = tuple(my_tuple) # Revertendo para Tupla novamente
print(my_tuple)
print(type(my_tuple))

del my_tuple
#print(my_tuple) --> name 'my_tuple' is not defined