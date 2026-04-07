class Churrasco:

    def __init__(self, nome="churras", pessoas=0):
        self.nome = nome
        self.pessoas = pessoas

    def analisar(self):
        print(
            f"Analisando {self.nome}...\nCada participante comerá 0.4 Kg de carne e cada Kg custa R$ 82.40\nRecomendo comprar {self.pessoas*0.40:.3f} Kg de carne\nO custo total será de R$ {82.40*(self.pessoas*0.40):.2f}\nCada pessoa pagará R$ {((self.pessoas*0.40)*82.40)/self.pessoas} para participar"
        )


c1 = Churrasco("Churras dos Parças", 15)
c1.analisar()
