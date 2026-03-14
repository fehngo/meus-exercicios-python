print("Hoje iremos analisar sua expressão e verificar se ela é valida ou não!")


lista = list()
abre = 0
fecha = 0
expressao = str(input("Digite sua expressão: "))
for i in expressao:
    if i == "(":
        abre += 1
    if i == ")":
        fecha += 1

if abre == fecha:
    print("Sua expressão é válida!")
else:
    print("Sua expressão é inválida!")
