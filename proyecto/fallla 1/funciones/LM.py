import numpy as np


invertir = [
    [(1, 0), (1, 2)],
    [(1, 1), (1, 1)],
    [(1, 2), (1, 0)],
    [(2, 0), (0, 2)],
    [(2, 1), (0, 1)],
    [(2, 2), (0, 0)],
    [(0, 0), (2, 2)],
    [(0, 1), (2, 1)],
    [(0, 2), (2, 0)]
]


def listTonumpy2d(List, RowColumns, Type):
    return np.resize(np.asarray(List, Type), RowColumns)


def buscarCamino(matriz, cond):
    print("detectando segmentos")
    Listp = list()
    r, c = getRowsColumns(matriz)
    for a in range(r):
        for b in range(c):
            if matriz[a, b] == cond:
                segmento, path = lengthPath(matriz, (a, b))
                Listp.append(segmento)
                for x in path:
                    matriz[x] = 0
    return Listp


# largo de segmento binaria
# matriz estandar
# First tuple posicion inicial
def lengthPath(matriz, First):
    transicion = 1
    path = list()
    pos = First
    last = pos
    path.append(pos)
    while(transicion):
        transicion, pos, last = moveposition(matriz, pos, last, 2)
        path.append(pos)
    primitivo = [
        First,
        last,
        len(path)
    ]
    print("\tprimitivo", primitivo)
    return primitivo, path


# matriz matriz estandar
# pos tupla ubicacion del puntero
# retorna tupla de la nueva posicion
# skip parametro opcional para omitir alguna posicion
def moveposition(array, pos, last, cond):
    r, c = pos
    m = [
        (r, c),
        (r, c - 1),
        (r, c + 1),
        (r + 1, c),
        (r - 1, c),
        (r - 1, c - 1),
        (r - 1, c + 1),
        (r + 1, c - 1),
        (r + 1, c + 1)
    ]
    m.remove(last)
    if (pos != last):
        m.remove(pos)
    for poss in m:
        if array[poss] >= cond:
            return 1, poss, pos
    return 0, poss, pos


# metodo getVecinos
# obtiene los vecinos de un posicion de matriz de tamaño 3x3
# array matriz numpy
# r entero numero de filas
# c entero nuemro de columnas
# retorna matriz 3x3
def neighboring3x3(array, r, c, centro=0):
    izq, der, arriba, abajo, arriba_izq, arriba_der, abajo_izq, abajo_der = [0 for _ in range(8)]
    b, a = 1, 1
    m = [[0 for _l in range(3)] for _p in range(3)]
    try:
        izq = array[r, c - 1]
    except:
        pass
    try:
        der = array[r, c + 1]
    except:
        pass
    try:
        arriba = array[r + 1, c]
    except:
        pass
    try:
        abajo = array[r - 1, c]
    except:
        pass
    try:
        arriba_izq = array[r - 1, c - 1]
    except:
        pass
    try:
        arriba_der = array[r - 1, c + 1]
    except:
        pass
    try:
        abajo_izq = array[r + 1, c - 1]
    except:
        pass
    try:
        abajo_der = array[r + 1, c + 1]
    except:
        pass

    m[a][b - 1] = izq
    m[a][b + 1] = der
    m[a + 1][b] = arriba
    m[a - 1][b] = abajo
    m[a - 1][b - 1] = arriba_izq
    m[a - 1][b + 1] = arriba_der
    m[a + 1][b - 1] = abajo_izq
    m[a + 1][b + 1] = abajo_der
    if centro:
        m[a][b] = array[a, b]
    return m


# metodo contarElemento
# obtiene los vecinos de un posicion de matriz de tamaño 3x3
# array matriz estandar
# r entero numero de filas
# c entero nuemro de columnas
# retorna entero numero de veces que se repite elementos
def countM(matriz, element):
    count = 0
    r, c = getRowsColumns(matriz)
    for a in range(r):
        for b in range(c):
            if matriz[a][b] == element:
                count += 1
    return count


def filtrerForElementM(matriz, element, columna, first=1, skip="no"):
    Rows, Columns = getRowsColumns(matriz)
    Listindex = list()
    if(skip == "no"):
        for r in range(Rows):
            if matriz[r][columna] == element:
                if(first):
                    return matriz[r]
                else:
                    Listindex.append(matriz[r])
    else:
        for r in range(Rows):
            for c in range(Columns):
                if (r, c) == skip: continue
                if matriz[r][c] == element:
                    if(first):
                        return matriz[r]
                    else:
                        Listindex.append(matriz[r])
    return Listindex


def getRowsColumns(matriz):
    r = len(matriz)
    c = len(matriz[0])
    return (r, c)


def sumM(matriz):
    road = 0
    count = 0
    r, c = getRowsColumns(matriz)
    for a in range(r):
        for b in range(c):
            road += 1
            count += matriz[a][b]
    return count


def printM(matriz):
    for a in matriz:
        print(a)


def inPosNeighboring(pos):
    for i in invertir:
        # print(i[0], pos)
        if i[0] == pos:
            # print(i[1])
            return i[1]
