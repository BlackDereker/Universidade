vel = float(input("Velocidade: "))

limite = 80

if vel <= limite:
    print("Nao foi multado")
else:
    multa = 0
    if vel > limite * 1.35:
        multa = 700
    elif vel >= limite * 1.21:
        multa = 580
    elif vel >= limite * 1.11:
        multa = 380
    else:
        multa = 180
    print("\nMulta: R$ %.2f" % multa)
