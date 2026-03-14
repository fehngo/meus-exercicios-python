## Criar lista principal e lista coletora de dados

pessoas = list()
dados = list()

## Criar um laço onde o captarei os dados e o usuário decidirá se quer continuar

while True:
    dados.append(input("Digite o nome: "))
    while True:
        try:
            dados.append(int(input("Digite o peso: ")))
            break
        except ValueError:
            print("Digite um número inteiro!")

    pessoas.append(dados[:])
    dados.clear()

    while True:
        decisao = input("Deseja continuar?[S/N]: ").upper().strip()
        if decisao in "SN":
            break
        else:
            continue

    if decisao == "N":
        break
    else:
        continue

## Mostrar quantas pessoas foram cadastradas

print(f"Foram cadastradas {len(pessoas)} pessoas.")

## Listar pessoas mais pesadas

pessoa_pesada = list()
maior_peso = pessoas[0][1]
pessoa_pesada.append(pessoas[0][0])

for d in pessoas:
    if d[1] > maior_peso:
        maior_peso = d[1]
        pessoa_pesada = [d[0]]
    elif d[1] == maior_peso and d[0] != pessoa_pesada[0]:
        pessoa_pesada.append(d[0])

print(f"O maior peso é {maior_peso} e percente a {pessoa_pesada}")

## Listar pessoas mais leves

pessoa_leve = list()
menor_peso = pessoas[0][1]
pessoa_leve.append(pessoas[0][0])

for d in pessoas:
    if d[1] < menor_peso:
        menor_peso = d[1]
        pessoa_leve = [d[0]]
    elif d[1] == menor_peso and d[0] != pessoa_leve[0]:
        pessoa_leve.append(d[0])

print(f"O menor peso é {menor_peso} e pertence a {pessoa_leve}")
