from random import randint

# from random import sample #importa o metodo sample do modulo random

while True:

    try:
        quantidade = int(input("Quantos números deseja que a tupla contenha? "))

        if quantidade > 0:
            break
        else:
            print("Digite um número maior que 0")

    except ValueError:
        print("Digite apenas números inteiros")


tupla_1 = tuple(randint(1, 10) for i in range(quantidade))
# tupla_2 = tuple(sample(range(1, 11), 5)) #Cria tupla sem repetição

print(f"Tupla com repetição {tupla_1}")
# print(f"Tupla sem repetição {tupla_2}") #Imprime tupla sem repetição
print(f"O maior número da tupla é {max(tupla_1)}")
print(f"O menor número da tupla é {min(tupla_1)}")
