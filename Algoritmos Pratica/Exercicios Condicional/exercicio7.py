ano = int(input("Digite o ano: "))
preco = float(input("Preco do carro: "))

if ano < 2010:
    print("Taxa: %.2f" % (preco * 0.025))
else:
    print("Taxa: %.2f" % (preco * 0.035))