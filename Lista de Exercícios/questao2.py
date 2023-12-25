#Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.

nota1 = float(input("Escreva a primeira nota: "))
nota2 = float(input("Escreva a segunda nota: "))

resultado = (nota1 + nota2)/2

if resultado >=6:
    print("Aprovado")
else:
    print("Reprovado")