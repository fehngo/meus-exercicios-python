## Importa date de detetime
from datetime import date

## Criar o dicionario matriz que armazenará a pessoa
funcionarios = list()

## Criar laço for para ler dados da pessoa
dados = dict()
dados["Nome"] = input("Digite o nome do funcionário: ")

while True:  ## Recebe e valida o ano de nascimento
    try:
        dados["Ano de Nascimento"] = int(input("Digite o ano de nascimento: "))
        break
    except ValueError:
        print("Digite um ano válido!")

while True:
    decisao = input("Você está empregado atualmente? [S/N]: ").upper().strip()
    if decisao in ["S", "N", "SIM", "NAO", "NÃO"]:
        break

if decisao[0] == "S":

    while True:  ## Recebe e valida a carteira de trabalho
        try:
            dados["Carteira"] = int(input("Digite o numero da carteira de trabalho: "))
            break
        except ValueError:
            print("Digite um número válido!")

    ###### Criar if para decidir perguntar ano de contratação e valor do salário
    while True:  ## Recebe e valida o ano de contratação
        try:
            dados["Ano de Contratacao"] = int(input("Digite o ano de contração: "))
            break
        except ValueError:
            print("Digite um valor válido!")

    while True:  ## Recebe e valida valor do salario
        try:
            dados["Salario"] = float(input("Digite em reais o valor do salário: "))
            break
        except ValueError:
            print("Digite um valor válido!")

    idade = date.today().year - dados["Ano de Nascimento"]
    dados["Aposentadoria"] = idade + 35

## Adiciona dados dentro da lista
funcionarios.append(dados.copy())

## Imprimir os dados com a condição se tiver carteira imprime salario e ano de contratação
print("-=" * 30)
for valor in funcionarios:
    for k, v in valor.items():
        print(f"   - {k} tem o valor {v}.")
