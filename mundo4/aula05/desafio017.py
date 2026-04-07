from rich import print
from rich.panel import Panel
from rich.align import Align


class Produto:
    def __init__(self, nome="generico", preco=0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return Panel(Align.center(f"{self.nome}\nR$ {self.preco:.2f}"), title="Produto")


p1 = Produto("Iphone", 3758.89)
print(p1.etiqueta())
