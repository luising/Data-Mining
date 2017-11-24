#Variables
step = 2 #Numero de pasos inicial
pos = 0 #Posicion actual del paso
tot = {} #Diccionario que contiene todas las combinaciones y el valor de apoyo
a = "ABCDBBCDABDCAABC" #String que se analizara
b = "" #Variable auxiliar
mayores = {}
mayor = 0

#Validaciones
if(step > len(a)):
  print("El numero de pasos no puede ser mayor que la longuitud de la cadena")

#Ciclo principal
for z in range(len(a)):
  if(step>(len(a)-8)):
        break
  print("--------------------------------")
  print("Tamaño de pasos = "+str(step))
  for j in range(len(a)):
    if(pos<=(len(a))-step):
      for i in range(step):
        b = b + a[i+j] #Variable auxiliar que contiene el elemento a comparar
      c = a.count(b) #Funcion que cuenta las veces que se repite el elemento 
      apoyo = (float(c)*float(step))/float(len(a))
      tot[b] = apoyo
      if mayor < apoyo:
        mayor = apoyo
      mayores[step] = mayor
        
      print(str(b)+" Frecuencia = "+str(c)+" Apoyo = "+str(apoyo))
      b = ""
      pos = pos + 1
    else:
      break
  step = step + 1
  pos = 0

#Impresiones
print("Mayores apoyos para cada paso")
print(mayores)

print("Fin del programa")
