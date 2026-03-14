try:
    quantidade = int(input('Quantas pessoas você deseja analisar? '))
    soma_idade = 0
    homem_velho = 0
    nome_velho = ''
    mulher20 = 0

    for i in range(0, quantidade):
        nome = input(f'Digite o nome da pessoa {i+1}: ').strip().title()
        idade = int(input(f'Digite a idade de pessoa {i+1}: '))
        sexo = input(f'Digite o sexo da pessoa (M/F) {i+1}: ').strip().upper()
        if idade <= 0:
            print('Insira idade maior que zero!')
            exit()
        elif sexo != 'M' and sexo != 'F':
            print('Insira o sexo M/F!')
            exit()
        else:
            soma_idade += idade
            if sexo == 'F' and idade < 20:
                mulher20 += 1
            if sexo == 'M' and idade > homem_velho:
                nome_velho = nome
                homem_velho = idade
    print(f'A média de idade desse grupo é de {soma_idade/quantidade} anos.')
    if nome_velho == '':
        print('Esta lista não contem nenhum homem!')
    else:
        print(f'O homem mais velho desse grupo é o {nome_velho}.')
    print(f'Esse grupo tem {mulher20} mulheres com menos de 20 anos.')

except ValueError:
    print('Insira valores válidos!')