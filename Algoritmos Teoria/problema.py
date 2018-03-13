vel = float(input("Velocidade: "))

limite = 80
multa = 0

if vel <= 80:
    print("Nao foi multado")
    exit()

if vel > limite * 1.35:
    multa = 700
elif vel >= limite * 1.21:
    multa = 580
elif vel >= limite * 1.11:
    multa = 380
else:
    multa = 180

print("\nMulta: R$ %.2f" % multa)
