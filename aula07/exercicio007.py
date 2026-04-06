print("O desafio dessa vez é calcular a média entre as nota dos 3 trimestres.")
nota1 = float(input("Qual a nota do primeiro trimestre?: "))
nota2 = float(input("Qual a nota do segundo trimestre?: "))
nota3 = float(input("Qual a nota do terceiro trimestre?: "))
media = (nota1 + nota2 + nota3) / 3
print(
    "A nota do primeiro trimestre foi {:.2f}, do segundo {:.2f}, e do terceiro {:.2f}.\nA média anual foi de {:.3f}.".format(
        nota1, nota2, nota3, media
    )
)
