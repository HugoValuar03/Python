class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0

    def calcula_media(self):
        self.media = (self.nota1 + self.nota2)/2
        return self.media
    
    def imprimeValoresAtributos(self):
        print('Seu nome é: ',self.nome)
        print('Sua nota 1 é: ',self.nota1)
        print('Sua nota 2 é: ',self.nota2)
        print('Sua média é: ',self.media)
        
    def aprovadoReprovado(self):
        if self.media >= 6.0:
            print('aprovado')
        else:
            print('reprovado')

aluno1 = Aluno('Hugo', 10.0, 5.0)
media = aluno1.calcula_media()
print()
aluno1.imprimeValoresAtributos()
print()
aluno1.aprovadoReprovado()