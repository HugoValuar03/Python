import pandas as pd

df = pd.DataFrame({'nome' : ['Fernando', 'Hugo', 'Higor'],
                   'idade' : [20,40,32]})

print(df)
print()
print(df.idade[1])
print(df.idade.mean())