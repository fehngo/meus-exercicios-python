'''print('Hoje iremos calcular uma progressão aritmética')

try:

    primeirotermo = int(input('Digite o primeiro termo da PA: '))
    razao = int(input('Digite a razão da PA: '))
    resultado = [primeirotermo]
    for c in range(0, 9):
        proximo = resultado[-1] + razao
        resultado.append(proximo)
    print(resultado)

except ValueError:
    print('Digite apenas valores inteiros!')'''

print('Hoje iremos calcular uma progressão aritmética!')

try:

    primeiro = int(input('Digite o primeiro termo da PA: '))
    razao = int(input('Digite a razão da PA: '))
    termo = int(input('Digite a quantidade de termos da PA: '))
    para = primeiro + ( termo - 1 ) * razao

    if termo <= 0:
        print('Numero de termos invalido!')

    else:
        for c in range(primeiro, para + razao, razao):
            print(c)

except ValueError:
    print('Digite apenas valores inteiros!')