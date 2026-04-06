"""from shlex import split

tentativa = str(input('Em qual cidade você nasceu ?: ')) .strip()
certo = 'santo'
tentativa = tentativa.lower()
tentativa = split(tentativa)

print(tentativa[0] == certo)"""

cidade = str(input("Em qual cidade você nasceu ?: ")).strip()
print(cidade[:6].lower() == "lorena")
