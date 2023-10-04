'''
En caso de no estar permitida la función sort para el ordenado de listas, 
se puede implementar un algoritmo de ordenamiento como el siguiente:

Se trataría del algortimo quicksort, que es un algoritmo de ordenamiento de complejidad O(nlog(n)).
'''

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivote = array[len(array) // 2]
    izquierda = [x for x in array if x < pivote] # elementos menores al pivote
    medio = [x for x in array if x == pivote] # elementos iguales al pivote
    derecha = [x for x in array if x > pivote] # elementos mayores al pivote
    
    return quick_sort(izquierda) + medio + quick_sort(derecha)

