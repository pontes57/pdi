# Plotagem de gráficos e imagens no notebook
#teste github
import matplotlib.pyplot as plt

# Manipulação de imagens
from PIL import Image
from skimage import color # Vamos usar para fazer uma conversão de espaço de cores específica
import imghdr # Vamos usar para verificar se um determinado arquivo em disco é uma imagem ou não
import cv2
import numpy as np # Manipulação de arrays
import os # Acesso ao sistema de arquivos do SO
import random # Geração de números aleatóriso. Você pode precisar em uma das atividades pedidas...

def hsl2rgb(arr):
    imgrgb=np.empty_like(arr)
    for x in range(arr.shape[0]):
        for y in range(arr.shape[1]):
            c=((1-abs(2*arr[x][y][2]-1))*arr[x][y][1])
            X=c*(1-abs(((arr[x][y][0]/60)%2)-1))
            m=arr[x][y][2]-(c/2)
            if 0<=arr[x][y][0]<60:
                imgrgb[x][y][0]=c
                imgrgb[x][y][1]=X
                imgrgb[x][y][2]=0
            elif 60<=arr[x][y][0]<120:
                imgrgb[x][y][0]=X
                imgrgb[x][y][1]=c
                imgrgb[x][y][2]=0
            elif 120<=arr[x][y][0]<180:
                imgrgb[x][y][0]=0
                imgrgb[x][y][1]=c
                imgrgb[x][y][2]=X
            elif 180<=arr[x][y][0]<240:
                imgrgb[x][y][0]=0
                imgrgb[x][y][1]=X
                imgrgb[x][y][2]=c
            elif 240<=arr[x][y][0]<300:
                imgrgb[x][y][0]=X
                imgrgb[x][y][1]=0
                imgrgb[x][y][2]=c
            elif 300<=arr[x][y][0]<360:
                imgrgb[x][y][0]=c
                imgrgb[x][y][1]=0
                imgrgb[x][y][2]=X
            imgrgb[x][y][0]=round((imgrgb[x][y][0]+m)*255)
            imgrgb[x][y][1]=round((imgrgb[x][y][1]+m)*255)
            imgrgb[x][y][2]=round((imgrgb[x][y][2]+m)*255)
    # Você pode alterar o retorno da função à vontade    
    return Image.fromarray(np.uint8(imgrgb))

def rgb2hsl(arr):
    imghsl=np.empty_like(arr,dtype=float)
    for x in range(arr.shape[0]):
        for y in range(arr.shape[1]):
            R=arr[x][y][0]/255
            G=arr[x][y][1]/255
            B=arr[x][y][2]/255
            maximo=max((R,G,B))
            minimo=min((R,G,B))
            delta=maximo-minimo
            imghsl[x][y][2]=(maximo+minimo)/2.0
            if delta==0:
                imghsl[x][y][0]=0
            elif maximo==R:
                imghsl[x][y][0]=((((G-B)/delta)%6)*60)
            elif maximo==G:
                imghsl[x][y][0]=((((B-R)/delta)+2)*60)
            elif maximo==B:
                imghsl[x][y][0]=((((R-G)/delta)+4)*60)
            imghsl[x][y][1]=(delta/(1-abs(2*imghsl[x][y][2]-1)))
    print(imghsl[127][52][:])
    return imghsl

img = Image.open(r'C:\Users\gabri\Documents\pdi\capivara.jpg')
img.show()
arr=np.asarray(img)
hsl=rgb2hsl(arr)
fator=2
f=fator-1
if f>=0:
    hsl[:][:][0]=hsl[:][:][0]+f*(1-hsl[:][:][0])* hsl[:][:][0]
else:
    hsl[:][:][0]=hsl[:][:][0]+f*hsl[:][:][0]
#img.show()
img=hsl2rgb(hsl)
#cv2.imwrite(r'C:\Users\gabri\Documents\pdi\capivarahsl.jpg', img)
img.show()
#img1 = cv2.imread(r'C:\Users\gabri\Documents\pdi\capivara.jpg')
#imgHLS = cv2.cvtColor(img1, cv2.COLOR_BGR2HLS)
#Image.fromarray(np.uint8(img)).show()
