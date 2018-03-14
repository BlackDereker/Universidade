text = input("Texto: ")

print("")

sequence = input("Sequencia: ")

count = 0

for word in text.split():
    temp = ""
    sequenceIndex = 0
    for i in range(len(word)):
        if word[i] == sequence[sequenceIndex]:
            sequenceIndex += 1
            temp += word[i]
            if temp == sequence:
                count += 1
                temp = ""
                sequenceIndex = 0
        else:
            temp = ""

print("\nA sequencia '%s' aparece %d vezes" % (sequence, count))