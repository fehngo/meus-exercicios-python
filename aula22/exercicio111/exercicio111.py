# Importar modulo moeda
from utilidadescev import moeda

# Ler um valor
p = moeda.ler_float("Digite um valor em reais: ")
moeda.resumo(p, 35, 22)
