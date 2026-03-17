## Esse código tem por finalidade criar um sistema de cadastro de notas de aluno, de forma que seja possivel ferificar a media e mais detalhes da media

## Criar a lista matriz
matriz = []
## Criar a entrada de nome, nota1, nota2 em uma lista e adicionar essa lista dentro da matriz
numeroord = 0
while True:
    dados = []
    numeroord += 1
    dados.append(numeroord)
    dados.append(input("Digite o nome do aluno: "))

    while True:
        try:
            dados.append(float(input("Digite a primeira nota do aluno: ")))
            break
        except ValueError:
            print('Digite apenas números inteiros ou separados por "."')

    while True:
        try:
            dados.append(float(input("Digite a segunda nota do aluno: ")))
            break
        except ValueError:
            print('Digite apenas números inteiros ou separados por "."')

    matriz.append(dados[:])
    dados.clear()

    while True:
        decisao = input("Deseja continuar? [S/N]: ").strip().upper()
        if decisao in "SsnN":
            break
        else:
            print('Digite apenas "S" ou "N"')

    if decisao in "nN":
        break
print(f"=-" * 21)

## Exibir formatado a media dos alunos
print(f"{'Nº ord':^8}| ", end="")
print(f"{"Nome":^22}| ", end="")
print(f"{"Média":^8}")

print(f"--" * 21)

for aluno in matriz:
    media = (aluno[2] + aluno[3]) / 2
    print(f"{aluno[0]:^8}| ", end="")
    print(f"{aluno[1]:<22}| ", end="")
    print(f"{media:^8}")


## Perguntar qual aluno deseja verificar e exibe detalhes do aluno
while True:
    while True:
        try:
            escolha = input("Deseja detalhar algum aluno?: [S/N]: ").strip().upper()
        except ValueError:
            print('Digite apenas "S" ou "N"!')
        if escolha in "SsNn":
            break

    encontrado = False
    if escolha in "Ss":
        while True:
            try:
                pergunta = int(input("Digite o número do aluno: "))
                break
            except ValueError:
                print("Digite o Nº Ord do aluno!!")

        for aluno in matriz:
            if aluno[0] == (pergunta):
                print(f"O as notas do aluno: {aluno[1]} são: {aluno[2]} e {aluno[3]}")
                encontrado = True
            if encontrado == False:
                print("Aluno não encontrado!")

    else:
        break
