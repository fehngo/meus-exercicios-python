# Criar a função
def notas(*n, sit=False):
    """
    -> Recebe várias notas e retorna um dicionário com:
       quantidade, maior, menor, média e situação (opcional)
    :param n: notas dos alunos
    :param sit: mostra ou não a situação
    :return: dicionário com dados das notas
    """
    dicionario = dict()

    dicionario["Total"] = len(n)
    dicionario["Maior"] = max(n)
    dicionario["Menor"] = min(n)
    dicionario["Média"] = sum(n) / len(n)

    if sit:
        if dicionario["Média"] < 6:
            dicionario["Situação"] = "Ruim"
        elif dicionario["Média"] < 7:
            dicionario["Situação"] = "Razoável"
        else:
            dicionario["Situação"] = "Boa"

    return dicionario


# Enviar as notas e rodar a função
resp = notas(5.5, 9.5, 10, 6.5)
print(resp)
