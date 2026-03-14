brasileirao = (
    "Palmeiras",
    "São Paulo",
    "Fluminense",
    "Bahia",
    "Corinthians",
    "Atletico PR",
    "Bragantino",
    "Chapecoense",
    "Mirassol",
    "Coritiba",
    "Flamengo",
    "Botafogo",
    "Gremio",
    "Vitória",
    "Atletico MG",
    "Remo",
    "Vasco da Gama",
    "Santos",
    "Internacional",
    "Cruzeiro",
)
print(f"Os 5 primeiros colocaso são: {brasileirao[0:5]}")
print(f"Os 4 ultimos colocados são: {brasileirao[-4:]}")
print(f"Os times participantes em ordem alfabetica são: {sorted(brasileirao)}")
time = input("Qual time deseja procurar? ").strip().title()
print(f"O time {time} esta na {brasileirao.index(time) + 1}º posição da tabela!")
