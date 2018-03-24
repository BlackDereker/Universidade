def maiorab(a, b):
    return (a + b + abs(a - b)) / 2


tokens = input().split(" ")

a = int(tokens[0])
b = int(tokens[1])
c = int(tokens[2])

first = maiorab(a, b)

result = maiorab(first, c)

print(int(result), "eh o maior")

