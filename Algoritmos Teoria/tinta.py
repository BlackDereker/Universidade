import math

areaPintada = float(input("Area que vai ser pintada: "))

litro = areaPintada / 3

latas = math.ceil(litro / 18)

print("Quantidade de Latas:", latas)

