import pandas as pd

df = pd.DataFrame({'nome' : ['Fernando', 'Hugo', 'Higor'],
                   'idade' : [20,40,32]})

df.loc[0, 'nome'] = 'Fernandinho' #Atualizar algum dado da coluna

print(df)


df['Sexo'] = ['F', 'M', 'F'] #Inserir nova coluna
print(df)