n = int(input()) # numero de peliculas
horarios = []
total = 0

for _ in range(n):
    a , b = map(int, input().split())
    horarios.append([a,b])

horarios.sort()
for i in range(n-1):
    if horarios[i][1] > horarios[i+1][0]:
        total += 1
        horarios[i+1][0] = horarios[i][0]
        horarios[i+1][1] = horarios[i][1]

print(total)
