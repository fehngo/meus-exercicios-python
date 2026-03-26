import funcoes
from time import sleep

tamanho = funcoes.cabecalho("MENU PRINCIPAL")
while True:
    escolha = funcoes.opções(
        "Listar Pessoas Cadastradas", "Cadastrar Nova Pessoa", "Sair do Sistema"
    )
    if escolha == 1:
        funcoes.cabecalho("Opção 1")
    elif escolha == 2:
        funcoes.cabecalho("Opção 2")
    elif escolha == 3:
        funcoes.cabecalho("Saindo do sistema... Até logo!")
        break
    else:
        print("Opção Invalida!")
    sleep(2)
