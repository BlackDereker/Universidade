tokens = input().split(" ")

a = float(tokens[0])
b = float(tokens[1])
c = float(tokens[2])

triangle = a * c / 2
circle = 3.14159 * c * c
trapezium = (a + b) * c / 2
square = b * b
rectangle = a * b

print("TRIANGULO: %.3f" % triangle)
print("CIRCULO: %.3f" % circle)
print("TRAPEZIO: %.3f" % trapezium)
print("QUADRADO: %.3f" % square)
print("RETANGULO: %.3f" % rectangle)