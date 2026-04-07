from rich import print


class Funcionario:

    empresa = "Banco FNC"

    def __init__(self, nome="vazio", setor="desconhecido", cargo="aleatório"):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __str__(self):
        return f"Olá, eu sou {self.nome}, {self.cargo} do setor {self.setor}."

    def apresentação(self):
        return f"Olá, eu sou [blue]{self.nome}[/], {self.cargo} do setor {self.setor} do {self.__class__.empresa}."


pessoa1 = Funcionario("Felippe", "Administrativo", "Gerente")
print(pessoa1.apresentação())
