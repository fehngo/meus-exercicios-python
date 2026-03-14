lanche = ("Hamburguer", "Suco", "Pizza", "Pudin", "Batata Frita")

for comida in lanche:
    print(f"Eu vou comer {comida}")

for comida in range(0, len(lanche)):
    print(f"Vou comer {lanche[comida]} na posição {comida}")

for pos, comida in enumerate(lanche):
    print(f"Vou comer {comida} na posição {pos}")

print(sorted(lanche))

print(f"Comi pra caramba!")

"""a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(4))"""
