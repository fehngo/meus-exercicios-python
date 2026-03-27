# Importar Sleep
# from time import sleep

# Importar modulo
from interface import menu, cabecalho
from arquivo import arquivoExiste, criar_arquivo, ler_arquivo

# Declarar arq
arq = "Python/aula23/exercicio115b/cursoemvideo.txt"
if not arquivoExiste(arq):
    criar_arquivo(arq)


# Chamar função menu
while True:
    resposta = menu("Listar Pessoa", "Cadastrar Pessoa", "Sair do Programa")
    if resposta == 1:
        ler_arquivo(arq)
    elif resposta == 2:
        cabecalho("Opção 2")
    elif resposta == 3:
        print("Saindo do Programa... Até Logo!")
        break
    else:
        print("Erro! Digite uma opção válida!")
