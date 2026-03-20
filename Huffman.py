
import numpy as np
def Huffman(tab):
    
    string=[]
    


    for l in range(0,tab.shape[0]):
        for j in range(0,tab.shape[1]):
            string.append(str(tab[l,j]))


# Création de noeuds 
    class NodeTree(object): 
        def __init__(self, left=None, right=None): 
            self.left = left 
            self.right = right 
        def children(self): 
            return (self.left, self.right)
        def nodes(self):
            return (self.left, self.right)
        def __str__(self): 
            return '%s_%s' % (self.left, self.right) 
    # Fonction principale d’implémentation du Codage de Huffman 
    def huffman_code_tree(node, left=True, binString=''):
        if type(node) is str: 
            return {node: binString} 
        (l, r) = node.children() 
        d = dict() 
        d.update(huffman_code_tree(l, True, binString + '0'))
        d.update(huffman_code_tree(r, False, binString + '1')) 
        return d 
    # Calcul des fréquences 
    freq = {} 
    for c in string: 
        if c in freq: 
            freq[c] += 1
        else: 
            freq[c] = 1
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True) 
    nodes = freq 
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2] 
        node = NodeTree(key1, key2) 
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    huffmanCode = huffman_code_tree(nodes[0][0])
    print(' Char | Huffman code ')  
    print('----------------------') 
    for (char, frequency) in freq:
        print(' %-4r |%12s' % (char, huffmanCode[char]))
    
    
    compt = 0
    liste =[]
    liste2=[]
    l1=[]
    produit =[]
    lt=0;
    #_______________________ calcul de taille avant la compression ________________________
    for s in string :
        compt = compt +1
    compt*=8


    # _________________________ Recuperation des freqences et les codes binaires de caracteres saisie par l'utilisateur_________________
  
    string = list(set(string))
    for char  in string:
        for i in range(len(freq)):
       
            if char == freq[i][0]:
                liste.append(huffmanCode[char])
                liste2.append(freq[i][1])
            
          
            
        for j in range(len(liste)):
            lt = len(liste[j])
            l1.append(lt)
    
    #---------------------- calcule de produit entre les freauences et langueur de chaque caractere  et les mettre dans une liste---------------
    for  item in range(0,len(liste)):
        p = l1[item]*liste2[item]
        
        produit.append(p)
      
    #---------------------- calcule la somme de liste produit par la multiplication ---------------
    s=0 
    somme =0 
    while s < len(produit):
        somme = somme + produit[s] 
        s+=1
    
    #---------------------calcule de gain de message------------------------------
    gain = (1-(compt/somme)) * 100
    
    file= open('files/Huffman_freq.txt','w')
    file2 =open('files/Nombre_bits.txt','w')
    #________________________Affichage 1________________________________
    print("____________________________________________________")
    print(f"la taille de cette matrice est : {compt} bits")
    print("____________________________________________________")
    
    file.write(str(liste2))
   
    print("____________________________________________________")
    file2.write(str(l1))
   
    print(f"Le Gain est   : 7{round(gain)} %")
    print("____________________________________________________")
    return ""




