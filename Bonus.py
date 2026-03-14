print(
    "Este programa tem como finalidade calcular quantas horas do curso eu ja conclui!"
)
total = float(input("Quantas horas o curso tem no total?: "))
concluidas = float(input("Quantos por cento do curso ja foi conluido?: "))
resultado = total * concluidas / 100
print("Você ja concluiu {} horas do curso até agora".format(resultado))
