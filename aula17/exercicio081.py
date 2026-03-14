print("Neste exercício analisaremos números digitados pelo usuário")

lista = []

while True:

    try:
        numero = int(input("Digite um número: "))
        lista.append(numero)
    except ValueError:
        print("Digite apenas números inteiros!")
        continue  # volta para o início do laço principal

    while True:
        decisao = input("Deseja continuar? [S/N]: ").strip().upper()

        if not decisao:
            continue

        decisao = decisao[0]

        if decisao in "SN":
            break
        else:
            print("Resposta inválida! Digite S ou N.")

    if decisao == "N":
        break

lista.sort(reverse=True)

print(f"Você digitou {len(lista)} elementos!")
print(f"Os valores digitados em ordem decrescente foram: {lista}")

if 5 in lista:
    print("O valor 5 está na lista.")
else:
    print("O valor 5 não está na lista.")
