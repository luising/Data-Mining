import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import tflearn
import random
from tkinter import *


def entrenamientoTensor():
    # input - shape 'None' Afirma que, el valor puede ser cualquier cosa, es decir, podemos alimentar en cualquier número de imágenes
    # input image
    x = tf.placeholder(tf.float32, shape=[None, 784])
    # input class
    y_ = tf.placeholder(tf.float32, shape=[None, 10])

    # Input Layer
    # reshaping input for convolutional operation in tensorflow
    # '-1' states that there is no fixed batch dimension, 28x28(=784) is reshaped from 784 pixels and '1' for a single
    # channel, i.e a gray scale image
    x_input = tf.reshape(x, [-1, 28, 28, 1], name='input')
    # first convolutional layer with 32 output filters, filter size 5x5, stride of 2,same padding, and RELU activation.
    # please note, I am not adding bias, but one could add bias.Optionally you can add max pooling layer as well
    conv_layer1 = tflearn.layers.conv.conv_2d(x_input, nb_filter=32, filter_size=5, strides=[1, 1, 1, 1],
                                            padding='same', activation='relu', regularizer="L2",
                                            name='conv_layer_1')

    # 2x2 max pooling layer
    out_layer1 = tflearn.layers.conv.max_pool_2d(conv_layer1, 2)

    # second convolutional layer
    conv_layer2 = tflearn.layers.conv.conv_2d(out_layer1, nb_filter=32, filter_size=5, strides=[1, 1, 1, 1],
                                            padding = 'same', activation='relu', regularizer="L2",
                                            name = 'conv_layer_2')
    out_layer2 = tflearn.layers.conv.max_pool_2d(conv_layer2, 2)
    # fully connected layer
    fcl = tflearn.layers.core.fully_connected(out_layer2, 1024, activation='relu')
    fcl_dropout = tflearn.layers.core.dropout(fcl, 0.8)
    y_predicted = tflearn.layers.core.fully_connected(fcl_dropout, 10, activation='softmax', name='output')


    #loss function
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y_predicted), reduction_indices=[1]))
    #optimiser -
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
    #calculating accuracy of our model
    correct_prediction = tf.equal(tf.argmax(y_predicted,1), tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    #session parameters
    sess = tf.InteractiveSession()
    #initialising variables
    init = tf.initialize_all_variables()
    sess.run(init)
    #number of interations
    iter=500
    batch_size=50

    for i in range(iter):
        #batch wise training
        x_batch, y_batch = data.train.next_batch(batch_size)
        _,loss=sess.run([train_step, cross_entropy], feed_dict={x: x_batch,y_: y_batch})
        #_, loss,acc=sess.run([train_step,cross_entropy,accuracy], feed_dict={x:input_image , y_: input_class})

        if i%500==0:
            Accuracy=sess.run(accuracy,
                               feed_dict={
                            x: data.test.images,
                            y_: data.test.labels
                          })
            Accuracy=round(Accuracy*100,2)
            print ("error : {} , presicion en prueba  : {} %" .format(loss, Accuracy))
            LtextProceso['text'] += "error :{}".format(loss) +", presicion en prueba:{} " .format(Accuracy)+"\n"
        elif i%100==0:
            print ("error : {}" .format(loss))
            LtextProceso['text'] +="error :{}" .format(loss) + "\n"
    validation_accuracy=round((sess.run(accuracy,
                                feed_dict={
                                 x: data.validation.images,
                                 y_: data.validation.labels
                                  }))*100,2)

    print ("Precisión en el conjunto de datos de validación: {}%".format(validation_accuracy))
    LtextPrecision['text'] += "{}%".format(validation_accuracy)
    test_image=np.reshape(imagen, [1,784])

    pred=(sess.run(y_predicted,
                   feed_dict={
                       x:test_image
                   }))
    predicted_class=np.argmax(pred)

    print ("Predicted class : {}" .format(predicted_class))
    LtextResultado['text'] += "{}" .format(predicted_class)





def botonClick():
	entrenamientoTensor()

root = Tk()

root.title("Proyecto")

Encabezado = Label(root, text="Reconocimiento, entrenamiento y prueba de numeros en una imagen")
Encabezado.grid(row=1, column=1)

data = input_data.read_data_sets("MNIST_data/", one_hot=True)
imgnum = random.randint(0, 10000)
#Una codificación en hot devuelve una matriz de ceros y unos. Uno corresponde a la clase
imagen = data.test.images[imgnum].reshape((28, 28))
plt.imshow(imagen) #Needs to be in row,col order
plt.savefig("img.png")
#Imagen
imgn = PhotoImage(file="C:\\Users\\luis\\Personal\\universidad\\Tareas\\redes neuronales\\Codigo\\img.png")
Limagen = Label(root, image = imgn, width = 225,height = 225)
Limagen.grid(row=3,column=1)
LtextPrecision = Label(root, text = "presicion :", relief="groove", borderwidth=5)
LtextPrecision.grid(row=4,column=2)
LtextProceso = Label(root, text = "Consola : \n", relief="groove", borderwidth=5)
LtextProceso.grid(row=5,column=1)
LtextResultado = Label(root, text = "resultado = ", relief="groove", borderwidth=5)
LtextResultado.grid(row=4,column=1)

#Boton
Boton = Button(root, text="Iniciar",bg='blue', command=botonClick)
Boton.grid(row=10,column=1)

root.mainloop()
