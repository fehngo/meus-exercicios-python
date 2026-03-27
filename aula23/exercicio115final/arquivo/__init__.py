def arquivo_existe(nome):
    try:
        with open(nome, "r"):
            pass
    except FileNotFoundError:
        return False
    else:
        return True


def criar_banco(nome):
    try:
        with open(nome, "w"):
            pass
    except Exception:
        print("Ocorreu um erro ao criar o banco de dados.")
    else:
        print("Banco de dados criado com sucesso.")


def listar_pessoas(nome):
    try:
        with open(nome, "r", encoding="utf-8") as arquivo:
            a = arquivo.readlines()
    except Exception:
        print("Ocorreu um erro ao abrir o banco de dados!")
        return []
    else:
        return a


def cadastrar_pessoas(banco, nome="<Desconhecido>", idade=0):
    try:
        with open(banco, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{nome};{idade}\n")
    except Exception:
        print(f"Ocorreu um erro ao adicionar o {nome} ao banco!")
    else:
        print(f"{nome} cadastrado com sucesso!")
