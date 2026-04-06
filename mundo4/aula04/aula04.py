class Gafanhoto:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade"


g1 = Gafanhoto()
g1.nome = "Felippe"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Stéffany"
g2.idade = 17
print(g2.mensagem())
