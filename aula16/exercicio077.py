tupla = (
    "Aprender",
    "Programar",
    "Linguagem",
    "Python",
    "Curso",
    "Gratis",
    "Estudar",
    "Praticar",
    "Trabalhar",
    "Mercado",
    "Programador",
    "Futuro",
)

for i in tupla:
    print(f"\nNa palavra {i.upper()} temos: ", end="")
    for letra in i:
        if letra.lower() in "aeiou":
            print(f"{letra.lower()}", end=" ")
