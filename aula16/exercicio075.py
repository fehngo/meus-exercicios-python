tupla_imutavel = (
    int(input("Digite um numero: ")),
    int(input("Digite outro número: ")),
    int(input("Digite o terceiro número: ")),
    int(input("Digite o ultimo número: ")),
)
tupla_par = tuple(i for i in tupla_imutavel if i % 2 == 0)

print(f"O valor '9' aparece {tupla_imutavel.count(9)} vezes.")
if 3 in tupla_imutavel:
    print(f"O número primeiro valor '3' aparece na {tupla_imutavel.index(3) + 1}ª posição ")
else:
    print("O valor 3 não aprece na tupla!")
print(f"Os valores pares desta tupla são {tupla_par}")
