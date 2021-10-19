lines = int(input())
X = 0

for operacion in range(lines):
    operacion = input()
    if operacion == '++X' or operacion == 'X++':
        X +=1
    else:
        X -=1
print(X)
