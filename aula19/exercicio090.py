## Criar dicionario Aluno
aluno = list()

## Criar estrutura que recebe nome e media do aluno e adiona no dicionario
while True:
    dados = dict()
    dados["Nome"] = input("Digite o nome do aluno: ")

    while True:
        try:
            dados["Média"] = float(input(f'Digite a media do {dados["Nome"]}: '))
            break
        except ValueError:
            print("Digite um valor válido para nota do aluno!")

    if dados["Média"] >= 7:
        dados["Situação"] = "Aprovado"
    elif 5 <= dados["Média"] < 7:
        dados["Situação"] = "Recuperação"
    else:
        dados["Situação"] = "Reprovado"

    aluno.append(dados.copy())

    while True:
        condicao = input("Deseja continuar? [S/N]: ").upper().strip()
        if condicao in "SN":
            break

    if condicao in "Nn":
        break

## Exibir situação do aluno
"""print("=-" * 20)
for i in aluno:
    for k, v in i.items():
        print(f"{k} é igual a {v}")
    print("=-" * 20)"""
for i in aluno:
    print(f"{i["Nome"]} teve média {i["Média"]:.1f} e está {i["Situação"]}.")
