## Empréstimo Bancario ##
from time import sleep
print('Bem vindo ao analisador automático de emprestimos !')
casa = float(input('Qual o valor da casa que você pretende comprar? '))
salario = float(input('Quanto você ganha atualmente? '))
tempo = float(input('Em quantos anos você pretende pagar esse emprestimo? '))
tempo2 = tempo * 12
prestacao = casa / tempo2
print('\033[1;97;43mAnalisando...\033[m')
sleep(3)
if prestacao > salario * 30 / 100:
    print('Infelizmente não poderemos aprovar o seu financiamento, a prestação ultrapassa 30% do seu salário')
#   print(prestacao, tempo, tempo2)
else:
    print('Parabens, seu emprestimo foi aprovado!')
    print('O valor da sua prestação sera de {}, e você pagara em {} prestações.'.format(prestacao, tempo2))
