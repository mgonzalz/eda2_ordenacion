n = int(input()) # numero de peliculas
horarios = []
total = 0

for _ in range(n):
    a , b = map(int, input().split())
    horarios.append([a,b])

horarios.sort()

hora_final = 0 # guardamos la hora final de la pelicula anterior
for inicio, final in horarios:
    if inicio >= hora_final:
        total += 1
        hora_final = final

print(total)
