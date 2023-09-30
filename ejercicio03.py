n = int(input()) # numero de peliculas
horarios = []
total = 0

for _ in range(n):
    a , b = map(int, input().split())
    horarios.append([a,b])

horarios.sort()
