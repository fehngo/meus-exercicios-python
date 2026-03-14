tabela = (
    "Gabinete de Banheiro",
    450.00,
    "Gabinete de Pia",
    865.50,
    "Armário 2 Portas",
    400.00,
    "Armário Superior",
    975.00,
    "Balcão Gavereiro",
    600.00,
    "Dispensa Vertical",
    950.00,
    "Gabinete do Tanque",
    475.00,
)
print("-" * 50)
print(f"{'TABELA DE PREÇOS':^50}")
print("-" * 50)
for i in range(0, len(tabela)):
    if i % 2 == 0:
        print(f"{tabela[i]:.<40}", end="")
    else:
        print(f"R$ {tabela[i]:>7.2f}")
print("-" * 50)
