# Importar interface e Arquivo
import interface, arquivo
from time import sleep

arq = "Python/aula23/exercicio115final/bancodedados.txt"
if not arquivo.arquivo_existe(arq):
    arquivo.criar_banco(arq)

while True:
    escolha = interface.menu("Listar Pessoas", "Cadastrar Pessoas", "Sair do Programa")
    if escolha == 1:
        interface.cabecalho("Listar Pessoas")
        leitura = arquivo.listar_pessoas(arq)
        for linha in leitura:
            nome, idade = linha.split(";")
            idade = idade.strip()
            print(f"{nome:<44}{idade:>10} Anos.")
        sleep(1)
    elif escolha == 2:
        interface.cabecalho("Cadastrar Pessoas")
        nome = input("Digite o nome da pessoa: ")
        idade = interface.leia_int(f"Quantos anos {nome} tem?: ")
        arquivo.cadastrar_pessoas(arq, nome, idade)
        sleep(1)
    elif escolha == 3:
        interface.cabecalho("Saindo do Programa... Até Logo!")
        sleep(1)
        break
