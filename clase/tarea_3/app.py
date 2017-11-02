# -*- coding: utf-8 -*-
from funciones.Mxlsx import *
import math as m


def ordenarxColumna(filas, primer, segundo):
    # parametros son las columnas que se van ordenar
    # Ordenamos las filas en función de el primero y en función del segundo.
    return filas.sort(key=itemgetter(primer, segundo))


def agruparxColumna(matriz, columna):
    # Agrupamos en función de la columna.
    grupos = {k: list(v) for k, v in groupby(matriz, itemgetter(columna))}
    return grupos


def getValueNivel(pos, deep, level=1):
    listw = []
    for a, vector in pos.items():
        if level == deep:
            listw += [vector] if type(vector) == int else [len(vector)]
        else:
            if(type(vector) == int): continue
            else: listw += getValueNivel(vector, deep, level + 1)
    return listw


def printGraf(grupos, state=""):
    for a, vector in grupos.items():
        if(type(vector) == int):
            print(state, a, "--->", vector)
        else:
            lenght = len(vector)
            print(state, a, "--->", lenght)
            if lenght > 1:
                printGraf(vector, state + "\t")
    return


def recursividad(grupos, nivel, Nmax, state=""):
    dic = {}
    for a, vector in grupos.items():
        lenght = len(vector)
        if lenght > 1:
            nivel = 1 if nivel == Nmax else nivel
            g = ordenarxColumna(vector, nivel + 1, nivel)
            g = agruparxColumna(vector, nivel + 1)
            dic[a] = recursividad(g, nivel + 1, Nmax, state + "\t")
        else:
            dic[a] = lenght
    return dic


datos = ReadLog("log.xlsx")
g = list()
listEntropy = []
for v in range(2, 10):
    datos.ordenar(v - 1, v)
    datos.agrupar(v - 1)
    g.append(recursividad(datos.grupos, v - 1, 9))
    E = 0
    for x in range(1, 7):
        d = getValueNivel(g[len(g) - 1], x)
        tot = len(d)
        for i in d:
            E -= i / tot * m.log(i / tot, 10)
    listEntropy.append(E)
print(listEntropy)
mejor = min(listEntropy)
mejorIndex = listEntropy.index(mejor)
print("grafo mas eficiente", mejorIndex)
printGraf(g[mejorIndex])
