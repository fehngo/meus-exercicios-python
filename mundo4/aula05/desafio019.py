from time import sleep


class Livro:

    def __init__(self, titulo, paginas):
        self.pagina = 1
        self.titulo = titulo
        self.paginas = paginas
        print(
            f"Você acabou de abrir o livro {self.titulo} que tem {self.paginas} paginas no total.\nVocê agora está na página {self.pagina}."
        )

    def avancar_paginas(self, quantidade):
        contador = 0
        for p in range(quantidade):
            if self.pagina == self.paginas:
                break
            else:
                self.pagina += 1
                contador += 1
                print(f"{self.pagina}  ->  ", end="", flush=True)
                sleep(0.35)
        print(f"Você avançou {contador} páginas e agora esta na {self.pagina}")
        if self.pagina == self.paginas:
            print(f"Você chegou ao final do livro {self.titulo}")
        sleep(1)


l1 = Livro("Harry Potter", 20)
l1.avancar_paginas(10)
l1.avancar_paginas(8)
l1.avancar_paginas(1)
