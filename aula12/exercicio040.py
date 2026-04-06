print("Valos calcular sua media!")
try:
    nota1 = float(input("Digite a sua primeira nota: "))
    nota2 = float(input("Digite a sua segunda nota: "))
    nota3 = float(input("Digite a sua terceira nota: "))
    if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10):
        print("Digite suas notas entre 0 e 10!")
    else:
        media = (nota1 + nota2 + nota3) / 3
        if media >= 7:
            media = (nota1 + nota2 + nota3) / 3
            print(f"Parabéns, sua média foi de {media:.2f} e você está APROVADO!")
        elif 5 <= media < 7:
            print(f"Quase, sua média foi de {media:.2f} e você está de RECUPERAÇÃO!")
        else:
            print(f"Sinto muito, sua média foi de {media:.2f} e você está REPROVADO!")

except ValueError:
    print("Nota inválida!")
