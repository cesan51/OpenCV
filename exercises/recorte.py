#Recorte, solo coserva la parte de la imagen seleccionada

import cv2
import numpy as np   #utilidad: operciones con matrices
import matplotlib.pyplot as plt  #para graficar y analizar


#Creacion de la matriz de 10 x 10 de 1 solo canal(Matriz)
#img = np.zeros((10,10,1), np.uint8)

#Creacion de la matriz de 10 x 10 de 3 canales(Matriz)
img = 100 * np.ones((10,10,3), np.uint8)
img2 = 100 * np.ones((10,10,3), np.uint8)

img[5, 6, 0] = 255
img[3, 9, 0] = 0
img[8, 6, 0] = 205

img[5, 6, 1] = 255
img[3, 9, 1] = 0
img[8, 6, 1] = 205

img[5, 6, 2] = 255
img[3, 9, 2] = 0
img[8, 6, 2] = 205



#img[2, 3] = 200


#Mostramos los valores numericos
print(img)

#Recorte
recorte = img[3:7, 3:7]

#Mostramos nuestra imagen
#plt.imshow(img, cmap='gray') #cmap es el mapa de color, en este caso de grisees
#plt.show()

fig = plt.figure()

# IMAGEN ORIGINAL
ax4 = fig.add_subplot(1,2,1)
ax4.imshow(img)
ax4.set_title("IMG")


# IMAGEN RECORTE
ax4 = fig.add_subplot(1,2,2)
ax4.imshow(recorte)
ax4.set_title("RECORTE")


plt.show()

cv2.waitKey(0)
#cv2.destroyAllWindows()