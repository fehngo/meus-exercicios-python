'''print("Caixa eletrônico")
valor = int(input("Digite o valor a ser sacado: "))

nota50 = valor // 50
resto50 = valor % 50

nota20 = resto50 // 20
resto20 = resto50 % 20

nota10 = resto20 // 10
resto10 = resto20 % 10

nota1 = resto10

print(
    f"""Para esse valor será liberado:
Notas 50 Reais: {nota50}
Notas 20 Reais: {nota20}
Notas 10 Reais: {nota10}
Notas 1 Real: {nota1}"""
)
'''

print("Caixa eletrônico")
valor = int(input("Digite o valor a ser sacado: "))

cedula = 50

while True:
    if valor >= cedula:
        quantidade = valor // cedula
        valor = valor % cedula
        print(f"Cedulas de R$ {cedula}: {quantidade}.")

    if cedula == 50:
        cedula = 20
    elif cedula == 20:
        cedula = 10
    elif cedula == 10:
        cedula = 1
    else:
        break
