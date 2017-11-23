"""Apriori ."""
import numpy as np
import funciones.apriori as ap
from funciones.Mxlsx import ReadLog


log = ReadLog("doc\log.xlsx")
data = np.array(log.filas)
data = data[:, 1:]
head = log.titulo
ListParameter = [6, 5, 4, "nan", 20, 100, 200, "nan", "nan"]

print("--Datos de el log--")

ap.setData(data, ListParameter)
ap.classifyItems(head)
ap.getRule()
