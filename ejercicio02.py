n, x = map(int, input().split()) #numero de niños; peso máximo de la góndola

p = list(map(int, input().split())) #pesos de cada niño

total = 0


for i in range(n):
    for j in range(i+1, n):
        if p[i] + p[j] <= x: #Cada góndola: 1 o 2 niños
            total += 1
            p[j] = 0
            break

print(total)
