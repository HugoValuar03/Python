### Dicionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre" : "Hugo", "Sobrenome" : "Valuar", "Idade" : 19, 1 : "Python"}

my_dict = {
    "Nome" : "Hugo",
    "Sobrenome" : "Valuar", 
    "Idade" : 19, 
    "Linguagens" : {"Python", "Swift", "Kotlin"},
    1 : 1.77
    }

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

my_dict["Nome"] = "Pedro" # Altera o nome existente

print(my_dict["Nome"])

print(my_dict[1])

my_dict["Rua"] = "Rua Valuar"
print(my_dict)
# Um dicionario é um tipo de estrutura que é possível armazenar dados do tipo chave valor