import math

tokens = input().split(" ")
tokens1 = input().split(" ")

x = float(tokens[0])
y = float(tokens[1])

x1 = float(tokens1[0])
y1 = float(tokens1[1])

distance = math.sqrt(math.pow(x1 - x, 2) + math.pow(y1 - y, 2))

print("%.4f" % distance)