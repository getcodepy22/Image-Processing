
groupe ="""



           _____________________________
           | Ce travail est realisé par :| 
           |                             |
           |    -ALICHE OMAR             |
           |                             |
           -------------------------------
"""

print(groupe)
print("____________________________ Traitement en Cours ____________________________")
try:
    
    from Recommandation import *
    from PIL import Image 

    import numpy as np
    import matplotlib.pyplot as plt
    from Huffman import *

    #Recuperer l'image
    img = Image.open('img.jpg') 

    #convertir l'image en tableau
    numpydata = np.asarray(img) 
  


    #classer chaque couleur dans un tableau puis dans des fichiers
    red = numpydata[:,:,0]
    green = numpydata[:,:,1]
    blue = numpydata[:,:,2]

    file = open('files/rouge.txt','w')
    file1 = open('files/vert.txt','w')
    file2 = open('files/blue.txt','w')
    file3 = open('files/R709.txt','w')
    file4 = open('files/R601.txt','w')
    file5 = open('files/MethodeSimple.txt','w')


    file.write(str(red))
    file1.write(str(green))
    file2.write(str(blue))
    file.close()
    file1.close()
    file2.close()
    tupl =list(green.shape)


    nv_gris =np.ndarray((tupl[0],tupl[1]),dtype=int)


    nv_gris1 =np.ndarray((tupl[0],tupl[1]),dtype=int)
    nv_gris2 =np.ndarray((tupl[0],tupl[1]),dtype=int)
    i=0


    #Recommandation 709
    while i <tupl[0]:
        j=0
        while j< tupl[1]:
            temp = recomondation709(red[i,j],green[i,j],blue[i,j])
            r2 =  recomondation601(red[i,j],green[i,j],blue[i,j])
            r3 = methodeSimple(red[i,j],green[i,j],blue[i,j])
       
       
            nv_gris[i,j] =temp
            nv_gris1[i,j]=r2
            nv_gris2[i,j]=r3
       
            j+=1
       
        i+=1
    

    file3.write(str(nv_gris))
    file4.write(str(nv_gris1))
    file5.write(str(nv_gris2))
    file3.close()
    file4.close()
    file5.close()



    print(histogramme(nv_gris,"Recommandation 709","red"))
    print(histogramme(nv_gris1,"Recommandation 601","green"))
    print(histogramme(nv_gris2,"Methode Simple","blue"))

    arrayToPIC(nv_gris,"Recommandation 709")
    arrayToPIC(nv_gris1,"Recommandation 601")
    arrayToPIC(nv_gris2,"MethodeSimple")

    #partie 2
    print(Huffman(nv_gris2))
except ModuleNotFoundError :
    print("         ____________________________ERREUR___________________________________________")
    print("        |Installer la library matplotlib en utilisant cette commande :                 |")
    print("        |          pip install matplotlib                                              |")
    print("        |                                                                              |")
    print("        |Installer la library  PIL en utilisant cette commande :                       |")
    print("        |          pip install PIL                                                     |")
    print("        |______________________________________________________________________________|")

