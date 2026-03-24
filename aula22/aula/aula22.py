# Importar moudlo
import uteis

# Ler numero inteiro
while True:
    try:
        num = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Digite apenas números inteiros!")

fat = uteis.fatorial(num)
print(f"O fatorial de {num} é {fat}.")
print(f"O dobro de {num} é {uteis.dobro(num)}")
print(f"O triplo de {num} é {uteis.triplo(num)}")
