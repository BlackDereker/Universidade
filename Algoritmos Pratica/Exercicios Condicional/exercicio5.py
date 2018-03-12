ano = int(input("Digite o ano: "))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print("O ano %d e bissexto" % ano)
else:
    print("O ano %d nao e bissexto" % ano)