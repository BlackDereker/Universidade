num = int(input("Digite um numero: "))

temp = abs(num)

print("")

if temp % 3 == 0 and temp % 5 == 0:
    print("O numero %d e divisivel por 3 e 5" % num)
elif temp % 3 == 0 and temp % 5 != 0:
    print("O numero %d e divisivel apenas pelo 3" % num)
elif temp % 3 != 0 and temp % 5 == 0:
    print("O numero %d e divisivel apenas pelo 5" % num)
else:
    print("O numero %d nao e divisivel pelo 3 nem o 5" % num)