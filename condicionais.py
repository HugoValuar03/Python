### Condicionais ###

my_condicion = False

if my_condicion: #É o mesmo que if my_condicion == True:
    print("Se executa a condição do if")
     

my_condicion = 5 / 5 

if my_condicion == 10: 
    print("Se executa a condição do segundo if")

if my_condicion > 10 and my_condicion < 20: 
    print("É maior que 10 e menor que 20")
elif my_condicion == 1:    
    print("É igual a 1")
else:
    print("É menor ou igual que 10 ou maior ou igual que 20")  
    
print("A execução continua")

my_string = "Minha cadeia de texto"

if my_string:
    print("My cadena de texto no es vacía")