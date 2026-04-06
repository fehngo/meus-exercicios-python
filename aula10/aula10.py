"""'ano = int(input('Quantos anos tem o seu carro? '))
if ano <= 5:
    print('Carro Novo')
else:
    print('Carro Velho')
print('Até a próxima!')"""

"""nome = str(input('Qual o seu nome? ')) .strip() .title()
if nome == 'Felippe':
    print('Que nome lindo você tem!')
else:
    print('Seu nome poderia ser melhor!')
print('Tenha um bom dia!')"""

nota1 = float(input("Digite a nota do primeiro semestre!: "))
nota2 = float(input("Digite a nota do segundo semestre!: "))
media = (nota1 + nota2) / 2
if media >= 7.5:
    print("A sua média foi {:.2f}. \nParabens, você esta aprovado!".format(media))
elif media >= 7 and media < 7.5:
    print("A sua média foi {:.2f}. \nPoxa, você esta de recuperação!".format(media))
else:
    print("A sua média foi {:.2f}. \nVocê esta reprovado!".format(media))
print("Tenha um exelente dia!")
