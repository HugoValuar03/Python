#Escreva um programa que resolva uma equação de segundo grau.   

import math

#ax² + bx + c
#b² - 4ac
#(-b +- raiz(delta))/ (2*a)

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b**2) - 4*a*c 

x1 = (-b + (delta ** (1/2))) / 2*a
x2 = (-b - (delta ** (1/2))) / 2*a

print("O delta vale:" ,delta)
print("O X1 vale:" , x1)
print("O X2 vale:" , x2)

