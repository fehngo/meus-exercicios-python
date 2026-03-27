# Criar função leia int
def leia_int(msg):
    while True:
        try:
            numero = int(input(msg))
            return numero
        except (ValueError, TypeError):
            print("O valor digitado não é válido")


# Criar função linha
def linha(tamanho=60):
    return "-" * tamanho


# Criar Função cabeçalho
def cabecalho(titulo, tlinha=60):
    print(linha(tlinha))
    print(titulo.center(tlinha))
    print(linha(tlinha))


# Criar função menu
def menu(*funcoes):

    while True:
        cabecalho("Menu de Interação")
        for i, v in enumerate(funcoes):
            print(f"{i+1} - {v}")
        print(linha())
        while True:
            escolha = leia_int("Escolha uma das opções acima: ")
            if escolha <= len(funcoes):
                return escolha
            else:
                print("Opção inválida, escolha uma das opções acima!")
                continue
