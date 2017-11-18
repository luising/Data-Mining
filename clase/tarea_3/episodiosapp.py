#Variables
step = 2 #Numero de pasos de placeholders AxxB etc
pos = 0
pos2 = 0
a = "AVCAYCAYC" #string principal
aux = ""
aux2 = ""
totales = [[] for _ in range(30)]
indx = 0 #Indice de matriz que contiene los datos totales //0 es el valor 1 es la las veces de incidencias 2 es el numero de placeholders
c = 0 #Variable para contar las veces de incidencias
temp = [] #Lista temporal que se usa para no guardar elementos repetidos
mayor = 0

for i in range(len(a)):
    if(step>=len(a)):
       break
       
    print("//////////////////////////////////////////////////////////////////")
    print("Placeholder de "+str(step))
    for j in range(len(a)):
        if((pos+j)<(len(a)-step)):
            aux = a[pos+j]+a[pos+j+step]
            for k in range(len(a)):
                if(pos2<(len(a)-step)):
                    aux2 = a[k]+a[k+step]
                    if(aux == aux2):
                        c = c + 1
                    pos2 = pos2 + 1
                else:
                    print(str(aux)+" Frecuecia = "+str(c))
                    #Lista temporal para validacion
                    temp.append(aux) #Elemento
                    temp.append(c) #Total de incidencias
                    temp.append(step) #Numero de placeholders
                    apoyo = float(c*(step+1))/float(len(a)) #Funcion de apoyo
                    temp.append(apoyo) #Apyo)
                    
                    #Validacion para no agregar valores repetidos
                    if(temp not in totales):
                        totales[indx].append(aux)
                        totales[indx].append(c)
                        totales[indx].append(step)
                        totales[indx].append(apoyo)
                        indx = indx + 1
                    c = 0
                    pos2 = 0
                    del temp[:]
                    break
        else:
            pos = 0
            break
    step = step + 1

#Obtener el mayor
for i in totales:
    if (len(i)!=0):
        if i[3]>mayor:
            mayor = i[3]

print(totales)
for i in totales:
    if (len(i)!=0):
        if(i[3]==mayor):
           print("Clave = "+str(i[0])+" Placeholders = "+str(i[2])+" Apoyo = "+str(i[3]))
print("Fin del programa")
