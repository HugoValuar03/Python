import pandas as pd

pessoas = pd.read_excel('C:\Users\hugov\OneDrive\Documentos\Valuar codes vs\Python\Pandas\caso_estudo.xlsx', sheet_name='pessoas')

covid = pd.read_excel('C:\Users\hugov\OneDrive\Documentos\Valuar codes vs\Python\Pandas\caso_estudo.xlsx', sheet_name='registros_covid')

print(pessoas)
print(covid)