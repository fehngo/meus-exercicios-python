class Gafanhoto:
    """
    Essa classe cria um gafanhoto que é uma pessoa que tem nome e idade

    Para cria uma nova pessoa use
    variavel = gafanhoto(nome, idade)
    """

    def __init__(self, nome="vazio", idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: Nome: {self.nome}; Idade: {self.idade}."


g1 = Gafanhoto("Felippe", 17)
g1.aniversario()
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)

g2 = Gafanhoto("Stéffany", 16)
g2.aniversario()
print(g2)

g3 = Gafanhoto()
print(g3)
