# Importar modulo moeda
import moeda

# Ler um valor
p = moeda.ler_float("Digite um valor em reais: ")
print(f"A metade de {p} é {moeda.metade(p)}")
print(f"O dobro de {p} é {moeda.dobro(p)}")
print(f"Aumentando 10%, temos {moeda.aumentar(p, 10)}")
print(f"Reduzindo 13%, temos {moeda.diminuir(p, 13)}")
