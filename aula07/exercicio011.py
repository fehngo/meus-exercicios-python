print("O desfio agora é calcular quanto de tinta é necessario para pintar uma parede.")
altura = float(input("Começaremos pela altura, Qual a altura da sua parede em metros: "))
largura = float(input("Agora preciso da largura da parede: "))
area = float(altura * largura)
tinta = area / 2
print(
    "A Área dessa parede é de {:.2f} m² e será necessário {:.2f} litros de tinta.".format(
        area, tinta
    )
)
