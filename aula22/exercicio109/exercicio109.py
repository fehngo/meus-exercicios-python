# Importar modulo moeda
import moeda

# Ler um valor
p = moeda.ler_float("Digite um valor em reais: ")
print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}")
print(f"Aumentando 10%, temos {moeda.aumentar(p, 10, True)}")
print(f"Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}")
