print("Este programa serve para analisar o sexo da pessoa:")
sexo = []
while sexo not in ("M", "F"):
    sexo = str(input("Digite o sexo da pessoa: ")).strip().upper()
print("Obrigado por participar!")
