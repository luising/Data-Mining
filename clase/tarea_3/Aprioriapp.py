"""librerias estandar."""
import numpy as np
from funciones.Mxlsx import ReadLog
from apyori import apriori

log = ReadLog("doc\log.xlsx")
data = np.array(log.filas)
factores = (2, 3, 19, 20)
data = data[:, 1:]
label = data.copy()
listLabel = []
Listcategoric = []

ListP = [6, 5, 4, "nan", 20, 100, 200, "nan", "nan"]
print("--Datos de el log--")


def rangeNumeric(c, v):
    """Clasificar Numerica."""
    keylist = list()
    lmin = int(float(min(label[:, c])))
    lmax = int(float(max(label[:, c])))
    lenR = ListP[c]
    key = 0
    limu = 0
    print("min: ", lmin, " max: ", lmax)
    for limB in range(lmin + lenR, lmax + 1, lenR):
        limA = limB - lenR
        limA = limA + 1 if limA != lmin else limA
        r = label[:, c]
        label[:, c][(r >= str(limA)) & (r <= str(limB))] = str(c) + str(key)
        key += 1
        limu = limB
        keylist.append(v + "[" + str(limA) + "-" + str(limB) + "]")
        print(" [", limA, "-", limB, "]")
    if limu != lmax:
        r = label[:, c]
        label[:, c][(r >= str(limu)) & (r <= str(lmax))] = str(c) + str(key)
        keylist.append(v + "[" + str(limu) + "-" + str(lmax) + "]")
        print(" [", limu, "-", lmax, "]")
    listLabel.append(keylist)


def rangeCategoric(c, v):
    """Clasificar Catgorica."""
    keylist = list()
    columna = label[:, c]
    listcategoric = np.unique(columna)
    for i, categoric in enumerate(listcategoric):
        columna[columna == categoric] = str(c) + str(i)
        keylist.append(v + "[" + categoric + "]")
    label[:, c] = columna
    listLabel.append(keylist)


def showLabel(tlabel):
    """Mostrar el valor de item."""
    cadena = ""
    for co in tlabel:
        coc = int(co[0])
        cof = int(co[1])
        cadena += " | " + listLabel[coc][cof]
    # print(cadena)
    return cadena


def classifyItems():
    """Clasificacion items."""
    # clasificar etiquetas
    for i, variable in enumerate(log.titulo):
        if i == 0:
            continue
        print("variable: ", variable)
        try:
            int(float(label[0, i - 1]))
        except ValueError:
            tipo = "Categorica"
            print("tipo: ", tipo)
            rangeCategoric(i - 1, variable)
            print("------------------------")
        else:
            tipo = "numerico"
            print("tipo: ", tipo)
            rangeNumeric(i - 1, variable)
            print("------------------------")


classifyItems()
results = list(apriori(label))
for r in results:
    print(showLabel(list(r[0])), " SOPORTE: ", r[1])
    print("\n", r[2])
