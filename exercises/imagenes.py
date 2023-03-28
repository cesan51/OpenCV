#Imagenes divididas como matrices por sus pixeles
#Cada uno de los pixeles tiene un valor entre 0 y 255, solo en escala de grises
#
#
#
#
#
#

import cv2
import numpy as np   #utilidad: operciones con matrices
import matplotlib.pyplot as plt  #para graficar y analizar


#Creacion de la matriz de 10 x 10 de 1 solo canal(Matriz)
#img = np.zeros((10,10,1), np.uint8)

#Creacion de la matriz de 10 x 10 de 3 canales(Matriz)
img = 100 * np.ones((10,10,3), np.uint8)

R = img[:, :, 0]
G = img[:, :, 1]
B = img[:, :, 2]

R [:, :] = 255
G [:, :] = 255
B [:, :] = 0


#img[2, 3] = 200


#Mostramos los valores numericos
print(img)

#Mostramos nuestra imagen
plt.imshow(img, cmap='gray') #cmap es el mapa de color, en este caso de grisees
plt.show()

#cv2.waitKey(0)
#cv2.destroyAllWindows()


