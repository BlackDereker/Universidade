kilometros = float(input("Kilometros percorridos: "))
dias = float(input("Dias que o carro foi alugado: "))

custo = kilometros * 0.15 + dias * 60

print("Custo: R$%.2f" % custo)
