from time import sleep

print("Hoje vamos analisar o seu triângulo")

try:
    reta1 = float(input("Digite o valor do primeiro segmento: "))
    reta2 = float(input("Digite o valor do segundo segmento: "))
    reta3 = float(input("Digite o valor do terceiro segmento: "))

    sleep(3)

    if reta1 <= 0 or reta2 <= 0 or reta3 <= 0:
        print("Você digitou segmentos negativos!")

    else:
        if reta1 < reta2 + reta3 and reta2 < reta3 + reta1 and reta3 < reta1 + reta2:
            print("Os Segmentos acima podem formar um triangulo")
            if reta1 == reta2 == reta3:
                categoria = "Equilátero"

            elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
                categoria = "Isósceles"

            else:
                categoria = "Escaleno"

            print(f"E esse triângulo é do tipo {categoria}!")

        else:
            print("Os segmentos acima não formam um triângulo")

except ValueError:
    print("Você digitou algum segmento inválido")
