arquivo = open("Arquivo.txt")

linhas = arquivo.readlines()
for linha in linhas:
    print(linha)
    
texto_completo = arquivo.readlines()
for linha in linhas:
    print(linha)
    
w = open("Arquivo2.txt", "w")
w.write("Esse eh o meu arquivo")
w.close