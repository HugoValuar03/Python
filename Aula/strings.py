'''
    Formatação de Strings
    
    • %s Strings
    • %d Inteiros
    • %f Floats
    
'''

# Exemplo
name = 'Hugo'
last_name = 'Valuar'
age = 19

print('Meu nome é %s %s e eu tenho %d anos' %(name, last_name, age))  

#Ou

print('Meu nome é {} {} e eu tenho {} anos' .format(name, last_name, age))  

# Inferencia de dados

print(f'Meu nome é {name} {last_name} e eu tenho {age} anos')  

#Imprimindo caracteres
language = 'pythOn'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Funções
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print(language.lower())
print(language.upper().isupper())