# Importar modulo moeda
from utilidadescev import dado, moeda

# Ler um valor
p = dado.leiaDinheiro("Digite um valor em reais: ")
moeda.resumo(p, 35, 22)
