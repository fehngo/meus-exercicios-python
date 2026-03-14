print("Cadastro de usuários!")

maior18 = homens = mulher20 = 0

while True:
    sexo = ""
    decisao = ""
    idade = int(input("Informe a idade: "))
    while sexo not in ["M", "F"]:
        sexo = input("Digite o sexo [M/F]: ").strip().upper()

    if idade > 18:
        maior18 += 1

    if sexo == "M":
        homens += 1

    if idade < 20 and sexo == "F":
        mulher20 += 1

    while decisao not in ["S", "N"]:
        decisao = input("Deseja continuar [S/N]: ").strip().upper()

    if decisao == "N":
        break

print(f"Você cadastrou {maior18} pessoas maiores de 18 anos.")
print(f"Você cadastrou {homens} homens.")
print(f"Você cadastrou {mulher20} mulheres menores de 20 anos.")
