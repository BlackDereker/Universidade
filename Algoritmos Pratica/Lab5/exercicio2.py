notas = (100, 50, 20, 10, 5, 2, 1)

valor = int(input("Digite o valor: "))


for i in range(len(notas)):
    numDeNotas = valor / notas[i]
    valor %= notas[i]
    print("Quantidade de notas %d: %d" % (notas[i], numDeNotas))
