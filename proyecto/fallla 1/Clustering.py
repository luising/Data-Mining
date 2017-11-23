import funciones.Mxlsx as m
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
