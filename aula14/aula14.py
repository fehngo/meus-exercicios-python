"""for c in range(1,5):
    int(input('Digite um valor: '))
print('FIM')"""

"""numero = ()
while numero != 0:
    numero = int(input('Digite um número: '))
print('FIM')"""

numero = 1
par = 0
impar = 0
while numero != 0:
    numero = int(input("Digite um valor: "))
    if numero != 0:
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"Você digitou {impar} números impar e {par} números pares")
