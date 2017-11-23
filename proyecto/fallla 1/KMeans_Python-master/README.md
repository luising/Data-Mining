# K-Means

El K-means es un método de Clustering que separa ‘K’ grupos de objetos (Clusters) de similar varianza, minimizando un concepto conocido como inercia, que es la suma de las distancias al cuadrado de cada objeto del Cluster a un punto ‘&mu;’ conocido como Centroide (punto medio de todos los objetos del Cluster).

Para saber más sobre el K-means, ir al siguiente tutorial:

http://jarroba.com/machine-learning-python-ejemplos/

## Pseudocódigo

A continuación se muestra el Pseudocódigo del K-means:

![alt jarroba](http://jarroba.com/wp-content/uploads/2016/05/KMeas_Pseudocodigo_jarroba.png)

## Diagrama de Clases

A continuación se muestra el diagrama de clases para la implementación del KMeans, en el que se ven involucradas las clases Point (Point.py) y Cluster (Cluster.py). En el script KMeans.py (que no es una clase aunque así se representa en el diagrama de clases) está el método Main que ejecuta el K-Means.
 
![alt jarroba](http://jarroba.com/wp-content/uploads/2016/05/KMeans_ClassDiagram_jarroba.png)

En el script KMeans_scikit.py se muestra una solución del K-Means utilizando la librería scikit-learn, por tanto no es una implementación propia (o desde cero) de este algoritmo.

## Prerrequisitos

El código que se encuentra en este repositorio hace uso de las librerías de numpy, matplotlib, scipy y scikit-learn. Para descargar e instalar (o actualizar a la última versión con la opción -U) estas librerías con el sistema de gestión de paquetes pip, se deben ejecutar los siguiente comandos:

```ssh
$ pip install -U numpy
$ pip install -U matplotlib
$ pip install -U scipy
$ pip install -U scikit-learn
```

## Resultados esperados de los data set

El orden de los clusters no tiene porque coincidir con los propuestos, pero los centroides si que deben de tener valores muy similares a los indicados:

![alt jarroba](http://jarroba.com/wp-content/uploads/2016/05/DataSet_info_clusters_jarroba.png)

### Resultados:

![alt jarroba](http://jarroba.com/wp-content/uploads/2016/05/Cluster3C.png)
![alt jarroba](http://jarroba.com/wp-content/uploads/2016/05/Cluster3C2.png)
![alt jarroba](http://jarroba.com/wp-content/uploads/2016/05/Cluster5C.png)
![alt jarroba](http://jarroba.com/wp-content/uploads/2016/05/Cluster7C.png)


Para más detalles del proyecto vista la web de jarroba.com:

![alt jarroba](http://jarroba.com/wp-content/themes/jarrobav6/static/img/logojarroba.png)
