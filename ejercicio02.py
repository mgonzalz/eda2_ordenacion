n, x = map(int, input().split()) #numero de niños; peso máximo de la góndola

p = list(map(int, input().split())) #pesos de cada niño

total = 0

p.sort()

inicio = 0

fin = n-1

while inicio <= fin:
    if inicio == fin:
        total += 1
        break
    if p[inicio] + p[fin] <= x:
        total += 1
        inicio += 1
        fin -= 1
    else:
        total += 1
        fin -= 1

print(total)
