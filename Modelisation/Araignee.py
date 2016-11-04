# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ce script temporaire est sauvegardé ici :
/home/romain/.spyder2/.temp.py
"""






from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np

def moveTo(vector):
    for i in range(len(listeObjets)):
        for j in range(len(listeObjets[i])):
            listeObjets[i][j]=np.add(listeObjets[i][j],vector)
    update(listeObjets)
    

def rotation(origine,vector,w):
    n=100
    vector=np.multiply(vector,(w/n))
    for j in range(len(listeObjets)):
        for m in range(len(listeObjets[j])):#changement de référentiel
            listeObjets[j][m]=np.subtract(listeObjets[j][m],origine)
        for i in range(n):
            for k in range(len(listeObjets[j])):
                print(listeObjets[j][k])
                print(np.cross(vector,listeObjets[j][k]))
                listeObjets[j][k]=np.add(listeObjets[j][k],np.cross(vector,listeObjets[j][k]))
                print(listeObjets[j][k])
        for m in range(len(listeObjets[j])):#changement de référentiel
            listeObjets[j][m]=listeObjets[j][m]+origine
    update(listeObjets)


def update(listeObjets):
    plt.clf()
    ax = Axes3D(fig)
    for objet in listeObjets:
        Coord=[]
        for a in range(3):
            Coord.append([])
            for b in range(len(objet)): 
                Coord[a].append(objet[b][a])
    
        ax.add_collection3d(Poly3DCollection([zip(Coord[0],Coord[1],Coord[2])]))
    ax.autoscale_view(None,True,True,True)
    ax.set_xlim3d(-100,100)
    ax.set_ylim3d(-100,100)
    ax.set_zlim3d(-100,100)
    plt.show()

def normalized(vector):
    return(vector/np.linalg.norm(vector))
        

#--------------Initialisation---------------
fig = plt.figure()
ax = Axes3D(fig)
plt.ion()
longueur=20
largeur=10
centre=[0,3,5]
NW=[centre[0]-largeur/2,centre[1]+longueur/2,centre[2]]
NE=[centre[0]+largeur/2,centre[1]+longueur/2,centre[2]]
SE=[centre[0]+largeur/2,centre[1]-longueur/2,centre[2]]
SW=[centre[0]-largeur/2,centre[1]-longueur/2,centre[2]]
listeObjets=[[NW,NE,SE,SW],[centre]]
ObjetParNom={}
ObjetParNom["plateforme"]=[NW,NE,SE,SW]
ObjetParNom["centre"]=[centre]
update(listeObjets)

#------------------------------------------
      
        
        
        
        
        
        
        