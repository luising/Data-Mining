import funciones.Mxlsx as m
from ejemplo.perceptron import Perceptron
import funciones.LM as lm

L = m.ReadLog("log.xlsx")
L.sort(2, 0)
L.agrupar(2)
grupos = L.grupos
Name_partidos = L.titulo[4:18]
# 0 año, 3 puesto
# 4 - 18 partidos
# 25 distrito, 26 hombre, 27 Mujer
# inicio 5


Ldistrito = "APODACA"
puesto = "Senador"
poblacion = m.ReadLog("poblacion.xlsx").getRows()
print(poblacion)

votosXanno = []
# print(Name_partidos)
for distrito, votos in grupos.items():
    if (distrito == Ldistrito):
        for d in votos:
            if(d[3] == puesto):
                votosXanno.append([v if v != "-" else 0 for v in d[4:18]])
# Creamos el perceptron
pr = Perceptron(15)  # Perceptron con 3 entradas
weights = []
for _ in range(3):
    for partidos in votosXanno:
        ganador = max(partidos)
        output = [a for a, s in enumerate(partidos) if s == ganador][0]
        p = lm.filtrerForElementM(poblacion, Ldistrito)[2:-3]
        _input = [elm / sum(partidos) for elm in partidos]
        genero = 1 if p[0] > p[1] else 0
        _input += [genero]  # Agregamos un uno por default
        print("entrada ", _input)
        weights.append(pr._w)
        err = pr.train(_input, output)
        print("error ", err)
test = []
# pre = pr.predict()
# print(pre)
