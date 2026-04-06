print("-=" * 20)
print("ANALISADOR DE TRIANGULO")
print("-=" * 20)
reta1 = float(input("Digite o primeiro segmento do triangulo: "))
reta2 = float(input("Digite o segundo segmento do triangulo: "))
reta3 = float(input("Digite o terceiro segmento do triangulo: "))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Os segmentos acima podem formar um triangulo")
else:
    print("Os segmentos acima não podem formar um triangulo")
