from random import shuffle
print('O programa de hoje irá escolher uma ordem para a apresentação do trabalho escolar')
alunos = []
for i in range(5):
    alunos.append(str(input('Digite o nome do Aluno: ')))
shuffle(alunos)
print('A ordem da apresentação do trabalho sera a seguinte {}'.format(alunos))