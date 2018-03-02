codes = {"A": "*-", "B": "-***", "C": "-*-*", "D": "-**", "E": "*", "F": "**-*", "G": "--*",
         "H": "****", "I": "**", "J": "*---", "K": "-*-", "L": "*-**", "M": "--", "N": "-*",
         "O": "---", "P": "*--*", "Q": "--*-", "R": "*-*", "S": "***", "T": "-", "U": "**-",
         "V": "***-", "W": "*--", "X": "-**-", "Y": "-*--", "Z": "--**",
         "1": "*----", "2": "**---", "3": "***--", "4": "****-", "5": "*****", "6": "-****",
         "7": "--***", "8": "---**", "9": "----*", "0": "-----"}

phrase = input("Frase: ")

words = phrase.split(" ")

morseCode = ""

for word in words:

    for letter in word:

        code = ""

        try:
            code = codes[letter.upper()]
        except KeyError:
            morseCode += "? "
            continue

        morseCode += code + " "

    morseCode += "\n"

print("\n" + morseCode)