import math
from turtle import color
from matplotlib import pyplot as plt
from PIL import Image 
import  numpy as np
from Huffman import *


#---------------------------------------------------------------------------------------
def recomondation709(red,green, bleu)->int:
    
    Gris = int(0.2125 * red + 0.7154 * green + 0.0721 * bleu)
    return Gris

#---------------------------------------------------------------------------------------
def recomondation601(red,green, bleu)->int:
    
    Gris = int(0.299 * red + 0.587 * green + 0.114 * bleu)
    return Gris

def methodeSimple(red,green,bleu)->int:
    Gris = int((red / 3 + green / 3 + bleu / 3))
    return Gris

#---------------------------------------------------------------------------------------
def histogramme(nv_gris,title,col):
    files= open('files/Histogramme.txt','w')
    nv_gris= nv_gris.astype(np.uint8)          # convertit les réels en octets

    # Calcule l'histogramme de l'image
    hist = np.zeros(256, int)       # prépare un vecteur de 256 zéros (pour chaque gris)
    for i in range(0,nv_gris.shape[0]):      # énumère les lignes
        for j in range(0,nv_gris.shape[1]):  # énumère les colonnes
            hist[nv_gris[i,j]] = hist[nv_gris[i,j]] + 1

    files.write(str(hist))
    print(f"la taille de ce fichier est :{len(hist)} octets")
    plt.xlabel("Pixel")
    plt.ylabel("Frequence")
    plt.title(title)
    plt.plot(hist,color=col)
    plt.show()
    return ""


#---------------------------------------------------------------------------------------
def arrayToPIC(nv_gris,name):
    data = Image.fromarray(nv_gris.astype('uint8'), 'L') 
    data.save(f'sorties/{name}.png')