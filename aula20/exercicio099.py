# importar a função sleep
from time import sleep


# Criar a função verificar maior
def maior(*num):
    contador = maior = 0
    print("Analisando os valores passados...")
    sleep(1.5)
    for v in num:
        print(f"{v}", end=" ", flush=True)
        if contador == 0:
            maior = v
            contador += 1
        else:
            if v > maior:
                maior = v
            contador += 1
    print(f"Foram informados {contador} valores ao todo. ")
    sleep(1.0)
    print(f"O maior valor informado foi {maior}.")
    print("-=" * 25)


# Programa
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
