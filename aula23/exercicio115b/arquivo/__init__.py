from interface import cabecalho


def arquivoExiste(nome):
    try:
        with open(nome, "rt"):
            pass
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        with open(nome, "w"):
            pass
    except Exception:
        print("Ocorreu um erro na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def ler_arquivo(nome):
    try:
        a = open(nome, "r", encoding="utf-8")
    except Exception:
        return print("Ocorreu um erro ao abrir o arquivo!")
    else:
        cabecalho("Listagem de Pessoas")
        print(a.read())
    finally:
        a.close()
