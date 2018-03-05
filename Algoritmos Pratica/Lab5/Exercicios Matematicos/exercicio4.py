import math

num = int(input("Digite o numero: "))
base = int(input("Digite a base: "))

print("\nLog de %d na base %d: %.3f" % (num, base, math.log(num, base)))