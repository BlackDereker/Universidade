vel = float(input("Velocidade: "))

limite = 80

multa = 0

if vel > limite:
    if vel > limite * 1.35:
        multa = 700
    elif vel >= limite * 1.21:
        multa = 580
    elif vel >= limite * 1.11:
        multa = 380
    else:
        multa = 180

print("")

if multa == 0:
    print("Nao foi multado")
else:
    print("Multa: R$ %.2f" % multa)
