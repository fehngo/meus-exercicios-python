import math

print("O programa de hore irá calcular o Seno, Cosseno e Tangente de um angulo")
angulo = float(input("Digite um angulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(
    "O angulo escolido foi {}° \nSendo assim temos: \nSeno {:.2f} \nCosseno {:.2f} \nTangente {:.2f}".format(
        angulo, seno, cosseno, tangente
    )
)
