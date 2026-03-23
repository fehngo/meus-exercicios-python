# Criar função que imprime mensagem adatada
def escreva(mensagem):
    tamanho = len(mensagem) + 2
    print("~" * tamanho)
    print(f"{mensagem:^{tamanho}}")
    print("~" * tamanho)


# Ler entrada da mensagem
entrada = input("Que mensagem deseja exibir?: ").strip()
escreva(entrada)
