import math

x = float(input("Coordenada X do primeiro ponto: "))
y = float(input("Coordenada Y do primeiro ponto: "))

x1 = float(input("Coordenada X do segundo ponto: "))
y1 = float(input("Coordenada Y do segundo ponto: "))

dist = math.sqrt(math.pow(x1 - x, 2) + math.pow(y1 - y, 2))

print("Distancia:", dist)