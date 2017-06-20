#!/usr/bin/env python3

# Autor: Elizabeth Gonzalez Romero y Brandon Estiven Moran Rojas
# Programa: ordenamiento.py
# Fecha: Sat Junio 17 10:11:12 COT 2017
# Descripcion: este programa ordena una lista por distintos metodos

import random, time

def aleatorios(n):
    """ (numero) -> (lista, lista, lista)

    retorna una lista de n numeros para cada caso: azar, ordenado, inverso

    """
    ordenado = list(range(0,n))
    azar = ordenado.copy()
    inverso = ordenado.copy()
    random.shuffle(azar)
    inverso.reverse()
    return (azar, ordenado, inverso)

def test(metodo, azar, ordenado, inverso):
    """ (funcion, lista, lista, lista) -> None
    
    Prueba el metodo de ordenamiento con una lista de tamano n
    
    """
    def prueba(metodo, lista):
        copia = lista.copy()
        ini = time.clock() # guarda la hora de inicio
        metodo(copia)
        fin = time.clock() # guarda la hora final
        return fin - ini
    t_azar = prueba(metodo, azar)
    t_ordenado = prueba(metodo, ordenado)
    t_inverso = prueba(metodo, inverso)
    print("{} ({}) : {:f}, {:f}, {:f}".format(metodo.__name__, n, t_azar, t_ordenado, t_inverso))

# Metodos de Ordenamiento

def insercion(lista):
    """ (lista) -> None
    
    ordena la lista por el metodo de insercion (Insertion)
    http://www.sorting-algorithms.com/insertion-sort
    
    >>> lista = [3, 6, 7, 4, 9, 2, 0, 8, 5, 1]
    >>> insercion(lista)
    >>> lista
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    """
    for i in range(1, len(lista)):
        k = i
        while k > 0 and lista[k] < lista[k-1]:
            # intercambia lista[k] y lista[k-1]
            lista[k], lista[k-1] = lista[k-1], lista[k]
            k-=1 # es igual a k=k-1

def seleccion(lista):
    """ (lista) -> None
    
    ordena la lista por el metodo de seleccion (Selection)
    http://www.sorting-algorithms.com/selection-sort
    
    >>> lista = [3, 6, 7, 4, 9, 2, 0, 8, 5, 1]
    >>> seleccion(lista)
    >>> lista
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    """
    n = len(lista)
    for i in range(0, n):
        k = i
        for j in range(i+1, n):
            if lista[j] < lista[k]:
                k = j
        # intercambia lista[i] y lista[k]
        lista[i], lista[k] = lista[k], lista[i]  


def burbuja(lista):
    """ (lista) -> None
    
    ordena la lista por el metodo de burbuja (Bubble)
    http://www.sorting-algorithms.com/bubble-sort
    
    >>> lista = [3, 6, 7, 4, 9, 2, 0, 8, 5, 1]
    >>> burbuja(lista)
    >>> lista
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    """
    n = len(lista)
    for i in range(0, n):
        swapped = False
        j = n - 1
        while j > i:
            if lista[j] < lista[j-1]:
                # intercambia lista[j] y lista[j-1]
                lista[j], lista[j-1] = lista[j-1], lista[j]
                swapped = True
            j -= 1
        if not swapped: break

def shell(lista):
    """ (lista) -> None
    
    ordena la lista por el metodo de shell (Shell)
    http://www.sorting-algorithms.com/shell-sort
    
    >>> lista = [3, 6, 7, 4, 9, 2, 0, 8, 5, 1]
    >>> shell(lista)
    >>> lista
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    """
    n = len(lista)
    for n in range(1, 0, n*3+1):
        while n>0:
            for i in range(0, n):
                j=i
                temp=lista[i]
                while j>=n and lista[j-n]>temp:
                    lista[j]=lista[j-n]
                    j=j-n
                lista[j]=temp
            n=n/2  

    
def merge(lista):
    """ (lista) -> None
    
    ordena la lista por el metodo de merge (Merge)
    http://www.sorting-algorithms.com/merge-sort
    
    >>> lista = [3, 6, 7, 4, 9, 2, 0, 8, 5, 1]
    >>> merge(lista)
    >>> lista
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    """
    i= 0
    j= 0
    arreglo =[]
    izq = []
    der = []
    n = len(lista)
    m = int(n / 2)
    for i in range(0, m):
        izq.append(lista[i])
    for i in range(m, len(lista)):
        der.append(lista[i])
    while(i < len(izq) and j < len(der)):
        if(izq[i] <= der[j]):
            arreglo.append(izq[i])
            i=i+1
        else:
            arreglo.append(der[j]);
            j=j+1
    while(i < len(izq)):
        arreglo.append(izq[i])
        i=i+1
    while(j < len(der)):
        arreglo.append(der[j])
        j=j+1

# recursive sorts
    

def heap(lista):
    """ (lista) -> None
    
    ordena la lista por el metodo de heap (Heap)
    http://www.sorting-algorithms.com/heap-sort
    
    >>> lista = [3, 6, 7, 4, 9, 2, 0, 8, 5, 1]
    >>> heap(lista)
    >>> lista
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    """
    for k in range(len(lista)-1,-1,-1):
        for i in range(len(lista),k):
            item=lista[i]
            j=(i+1)/2
            while j>=len(lista) and lista[j]<item:
                lista[i]=lista[j]
                i=j
                j=j/2
            lista[i]=item
        temp=lista[0];
    lista[0]=lista[k];
    lista[k]=temp;

   
def quick(lista):
    """ (lista) -> None
    
    ordena la lista por el metodo de quick (Quick)
    http://www.sorting-algorithms.com/quick-sort
    
    >>> lista = [3, 6, 7, 4, 9, 2, 0, 8, 5, 1]
    >>> quick(lista)
    >>> lista
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    """
    menor = []
    igual = []
    mayor = []
    if len(lista) > 1:
        pivot = lista[0]
        for x in lista:
            if x < pivot:
                menor.append(x)
            if x == pivot:
                igual.append(x)
            if x > pivot:
                mayor.append(x)
    
   
# Programa Principal
for n in [100, 1000,10000]:
    azar, ordenado, inverso = aleatorios(n)
    test(insercion, azar, ordenado, inverso)
    test(seleccion, azar, ordenado, inverso)
    test(burbuja, azar, ordenado, inverso)
    test(shell, azar, ordenado, inverso)
    test(merge, azar, ordenado, inverso)
    test(heap, azar, ordenado, inverso)
    test(quick, azar, ordenado, inverso)