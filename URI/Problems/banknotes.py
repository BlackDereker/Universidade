value = int(input())

print(value)

nota100 = value // 100
value %= 100

nota50 = value // 50
value %= 50

nota25 = value // 25
value %= 25

nota10 = value // 10
value %= 10

nota5 = value // 5
value %= 5

nota2 = value // 2
value %= 2

nota1 = value // 1
value %= 1


print("%d nota(s) de R$ 100,00" % nota100)
print("%d nota(s) de R$ 50,00" % nota50)
print("%d nota(s) de R$ 20,00" % nota25)
print("%d nota(s) de R$ 10,00" % nota10)
print("%d nota(s) de R$ 5,00" % nota5)
print("%d nota(s) de R$ 2,00" % nota2)
print("%d nota(s) de R$ 1,00" % nota1)