nome = input("Primeiro nome: ")
nome1 = input("Segundo nome: ")

first = ""
second = ""

if nome == nome1:
    print("\n" + nome + " - " + nome1)
    exit()

for i in range(len(nome) if len(nome) < len(nome1) else len(nome1)):
    if ord(nome[i]) < ord(nome1[i]):
        first = nome
        second = nome1
        break
    elif ord(nome1[i]) < ord(nome[i]):
        first = nome1
        second = nome
        break

if first == "":
    if len(nome) < len(nome1):
        first = nome
        second = nome1
    else:
        first = nome1
        second = nome

print("\n" + first + " - " + second)