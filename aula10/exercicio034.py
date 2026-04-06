salario = float(input("Qual o valor do salário do funcionario? "))
if salario <= 1250:
    salario = salario + (salario * 15 / 100)
else:
    salario = salario + (salario * 10 / 100)

print("O aumento de salário desse funcionário será de R${:.2f}".format(salario))
