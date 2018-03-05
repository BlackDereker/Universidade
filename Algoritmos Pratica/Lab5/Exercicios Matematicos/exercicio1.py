import math

num = int(input("Digite um numero: "))

print("")

for i in range(1, 10):
    print("\n%d elevado a %d: %d" % (num, i, math.pow(num, i)))