def leiaDinheiro(mensagem):
    valido = False
    while not valido:
        dinheiro = str(input(mensagem)).replace(",", ".").strip()
        if dinheiro.isalpha() or dinheiro == "":
            print(f'Erro, "{dinheiro}" não é válido!')
        else:
            valido = True
            return float(dinheiro)
