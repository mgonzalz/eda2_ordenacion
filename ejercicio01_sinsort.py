t = int(input()) #casos de prueba

while (t != 0):
    n = int(input()) #numero de alumnos
    a = list(map(int, input().split())) #identificador de los alumnos
    a = list(set(a))
    print(len(a))
    t= t-1
