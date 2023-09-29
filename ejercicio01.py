t = int(input()) #casos de prueba

while (t != 0):
    n = int(input()) #numero de alumnos
    a = list(map(int, input().split())) #identificador de los alumnos
    total = n
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            total -= 1
    print(total)
    t= t-1
