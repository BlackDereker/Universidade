import random
from myutils import *

def puzzle(switch):
    prize = random.randint(1, 3)
    choice = random.randint(1, 3)
    return (prize == choice and not switch) or (prize != choice and switch)


tries = int(input("Numero de tentativas: "))

if tries < 1:
    exit()

change = ""

while True:
    change = input("Trocar de porta (s/n): ").lower()
    if change == "s" or change == "n":
        break
    print("\nPor favor, responda com 's' ou 'n'\n")

print("")

wins = 0
for i in range(tries):
    success = puzzle(change == "s")
    fixedprint(str(i + 1) + ": ", "Success" if success else "Failure", 10)
    if success:
        wins += 1


lost = tries - wins

print("\n" + "Wins: %d | %.2f" % (wins, wins / tries * 100))
print("Lost: %d | %.2f" % (lost, lost / tries * 100))
