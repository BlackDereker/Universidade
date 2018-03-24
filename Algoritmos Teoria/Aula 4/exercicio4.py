compra = float(input("Valor da compra: "))

valor = 0

if compra < 20:
    valor = compra * 1.45
else:
    valor = compra * 1.3

print("\nValor de venda: %.2f" % valor)
