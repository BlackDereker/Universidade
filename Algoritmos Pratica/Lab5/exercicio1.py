num = int(input("Digite o numero: "))

divisor = 10 ** (len(str(num)) - 1)

while divisor >= 1:
    print(int(num / divisor))
    num %= divisor
    divisor /= 10
