product1 = input()
product2 = input()

tokens1 = product1.split(" ")
tokens2 = product2.split(" ")

units1 = int(tokens1[1])
price1 = float(tokens1[2])

units2 = int(tokens2[1])
price2 = float(tokens2[2])

total = units1 * price1 + units2 * price2

print("VALOR A PAGAR: R$ %.2f" % total)