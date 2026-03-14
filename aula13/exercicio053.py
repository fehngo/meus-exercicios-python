import unicodedata
print('Vamos verificar se uma frase é um palindromo.')

try:
    frase = input('Digite uma frase: ') .strip() .lower()
    semespaço = frase.replace(' ','')
    nova_frase = ''.join(
        c for c in unicodedata.normalize('NFKD', semespaço)
        if not unicodedata.category(c) == 'Mn'
    )
    print(nova_frase)

    if nova_frase == nova_frase[::-1]:
        print('Esta frase é um palindromo!')
    else:
        print('Esta frase não é um palindromo!')

except ValueError:
    print('Digite um valor válido!')