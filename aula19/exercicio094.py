# Criar Funções


# Criar Dicionário
pessoas = list()
dados = dict()

# Criar loop para adicionar dados no docionário
while True:
    dados["Nome"] = input("Digite o nome: ")

    while True:
        sexo = input("Digite o sexo: [M/F]: ").upper().strip()
        if sexo in "MF":
            dados["Sexo"] = sexo
            break
        else:
            print('Digite apenas "M" ou "F" !!')

    while True:
        try:
            dados["Idade"] = int(input("Digite a idade: "))
            break
        except ValueError:
            print("Digite um valor inteiro!!")

    pessoas.append(dados.copy())
    dados.clear()

    while True:
        decisão = input("Deseja continuar [S/N]: ").upper().strip()
        if decisão in "SN":
            break
        else:
            print('Digite apenas "S" e "N"!!')

    if decisão in "N":
        break

# Imprimir quantas pessoas
print("-=" * 45)
print(f" A - ) Ao todo temos {len(pessoas)} cadastradas.")

# Imprimir a média de
soma = 0
for valor in pessoas:
    for k, v in valor.items():
        if k == "Idade":
            soma += v
media = soma / len(pessoas)
print(f" B - ) A média de idade é de {media}.")

# Imprimir nome das mulheres cadastradas
mulheres = []
print(" C - ) As mulheres cadastradas foram: ", end="")
for valor in pessoas:
    if valor["Sexo"] == "F":
        mulheres.append(valor["Nome"])
print(", ".join(mulheres))
print("")

# Imprimir lista das pessoas acima da média
print(" D - ) Lista de pessoas que estão acima da média:")
for v in pessoas:
    if v["Idade"] > media:
        print(f'Nome: {v["Nome"]}; Sexo: {v["Sexo"]}; Idade: {v["Idade"]}.')

# Imprimir um << Encerrado >>
print("<<< Encerrado >>>")
