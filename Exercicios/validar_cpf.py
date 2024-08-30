"""
Cálculo do primeiro dígito

CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma 
contagem regressiva começando de 10

Ex.: 746.824.890-70 (746824890)
    11  10  9  8  7  6  5 4  3  2 
*   7   4  6  8  2  4  8  9  0  7
    70  36 48 56 12 20 32 27 0  14
    
Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
    
O primeiro dígito do CPF é 7
"""

cpf = '78698867006'\
    .replace(',', '') \
    .replace('-', '') \
    .replace(' ', '')
nove_digitos = cpf[:9]
contador_regressivo = 10
resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo
    contador_regressivo -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = cpf[:10]
contador_regressivo_2 = 11
resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

if (digito_1 == int(cpf[9:10])) and (digito_2 ==int(cpf[10:11])):
    print('Seu cpf é válido')
else:
    print('Seu cpf é inválido')