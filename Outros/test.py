b = 0

with open("Screenshot_5.png", "rb") as imageFile:
    f = imageFile.read()
    b = bytearray(f)

pixels = []
print(len(b))

pixelIndex = 0
for i in range(len(b)):
    if i != 0 and i % 3 == 0:
        pixelIndex += 1
    pixels.append()

