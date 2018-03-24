num = float(input("Digite o primeiro numero: "))
num1 = float(input("Digite o segundo numero: "))

print("\nMaior: ", end="")

if num > num1:
    print(num)
elif num1 > num:
    print(num1)
else:
    print(num, "e", num1, "sao iguais")
