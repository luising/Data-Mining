import funciones.LM as lm
import funciones.Values as v
import numpy as np

inputs = v.vp
funciones = ["exponential b^x", "Logarithmic log(x)", "trigonometric: Sin(x)", "trigonometric: Cos(x)", "trigonometric: Tan(x)"]

t = np.array(inputs)
x = t[:, 0]
y = t[:, 1]
# obtener exponencial
exp = 3 ** x
# obtener Logarithmic
log = np.log(x)
# obtener trigonometric
sin = np.sin(x)
cos = np.cos(x)
tan = np.tan(x)

err = []
err.append(abs(sum(np.abs(exp) - y)))
err.append(abs(sum(np.abs(log) - y)))
err.append(abs(sum(np.abs(sin) - y)))
err.append(abs(sum(np.abs(cos) - y)))
err.append(abs(sum(np.abs(tan) - y)))
salida = np.array([exp, log, sin, cos, tan])
bestfunction = funciones[err.index(min(err))]

print("---Funcion mas optima---")
print(bestfunction)
print("salida: ", salida[index])
print("y :", y)
