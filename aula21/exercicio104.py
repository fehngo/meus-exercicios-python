# Criar função
def leiaint(msg):
    while True:
        try:
            numero = int(input(msg))
        except ValueError:
            print("ERRO! Digite um número inteiro válido.")
        else:
            return numero


# Executar função e ler entrada do usuário
n = leiaint("Digite um número: ")

# imprimir o número
print(f"Você acabou de digitar o número {n}")
