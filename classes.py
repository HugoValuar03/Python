### Classes ###

class MyEmptyPerson:
    pass 

class Person:
    def __init__(self, nome, sobrenome):
        self.full_name = f"{nome} {sobrenome}"
        self.nome = nome
        self.sobrenome = sobrenome
    
    def walk(self):
        print(f"{self.full_name} está caminhando")
    
my_person = Person("Hugo", "Valuar")
print(f"{my_person.nome} {my_person.sobrenome}")
print(my_person.full_name)
my_person.walk()