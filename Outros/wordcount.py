text = input("Texto: ")

print("")

word = input("Palavra: ")

count = 0
for w in text.split():
    if w == word:
        count += 1

print("\nA palavra '%s' aparece %d vezes" % (word, count))
