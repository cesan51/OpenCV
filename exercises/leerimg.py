#Imagenes divididas como matrices por sus pixeles
#Cada uno de los pixeles tiene un valor entre 0 y 255, solo en escala de grises

import cv2
import numpy as np   #utilidad: operciones con matrices
import matplotlib.pyplot as plt  #para graficar y analizar

#Lectura e imagenes, lectura en Gray
imggray = cv2.imread("cesan.png", 0) # 1 canal 1 matriz

#Lectura e imagenes, lectura a color
imgRGB = cv2.imread("cesan.png", 1) # 3 canales 3 matrices

#Lectura e imagenes, lectura a color
img = cv2.imread("cesan.png") # 3 canales 3 matrices


#Extraer atributos principales

tema = imggray.shape
tipo = imggray.dtype

print("Tamaño Gray 1 Tipo de dato 1", tema, tipo)


#Mostrar las imagenes

cv2.imshow("GRAY", imggray)
cv2.imshow("RGB", imgRGB)
cv2.imshow("IMG", img)


#Mostramos nuestra imagen
plt.imshow(img)
plt.show()

cv2.waitKey(0)
#cv2.destroyAllWindows()


