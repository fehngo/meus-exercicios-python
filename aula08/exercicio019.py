from random import choice

print("O objetivo do codigo de hoje é realizar um sorteio entre os nomes")
n1 = str(input("Digite o nome do primeiro aluno: "))
n2 = str(input("Digite o nome do segundo aluno: "))
n3 = str(input("Digite o nome do terceiro aluno: "))
n4 = str(input("Digite o nome do quarto aluno: "))
n5 = str(input("Digite o nome do quinto aluno: "))
lista = [n1, n2, n3, n4, n5]
print("O nome sorteado foi {}".format(choice(lista)))
