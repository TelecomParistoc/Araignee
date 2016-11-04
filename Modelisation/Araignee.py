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

def moveTo(vector,ObjetsABouger):
    for i in range(len(ObjetsABouger)):
        for j in range(len(ObjetsABouger[i])):
            ObjetsABouger[i][j]=np.add(ObjetsABouger[i][j],vector)
    #update(listeObjets)
    

def rotation(origine,vector,w,objetsAPivoter):#w = angle de rotation, vector= vecteur directeur de l'axe de rotation
    n=50
    vector = normalized(vector)
    vector=np.multiply(vector,(w/n))
    for j in range(len(objetsAPivoter)):
        for m in range(len(objetsAPivoter[j])):#changement de référentiel
            objetsAPivoter[j][m]=np.subtract(objetsAPivoter[j][m],origine)
        for i in range(n):
            for k in range(len(objetsAPivoter[j])):
                objetsAPivoter[j][k]=np.add(objetsAPivoter[j][k],np.cross(vector,objetsAPivoter[j][k]))
        for m in range(len(objetsAPivoter[j])):#changement de référentiel
            objetsAPivoter[j][m]=objetsAPivoter[j][m]+origine
    #update(listeObjets)


def update(listeObjets):
    ax.cla()
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
    plt.pause(0.00000001)
    
def normalized(vector):
    return(vector/np.linalg.norm(vector))
    
def Time(iterations):
    global vitesse,motSpeedList
    for i in range(iterations):
        if not contact:
            vitesse[2]-=g*dt*100# en cm.s-1
        moveTo(np.multiply(vitesse,dt),listeObjets)
        """"
        for a in range(4):
            if motSpeedList[a][1]!=0:
                rotation(ObjetParNom["plateforme"][a],[0,0,1],motSpeedList[a][1],ObjetParNom["patte"+str(a)])"""
        testContact()
        update(listeObjets)
    

def testContact():
    global contactNW,contactNE,contactSE,contactSW,contact,vitesse
    i=0
    n=len(ObjetParNom["supportNW"])
    while i<n and not contactNW:
        if ObjetParNom["supportNW"][i][2]<=0:
            contactNW=True
        i+=1
    i=0
    while i<n and not contactNE:
        if ObjetParNom["supportNE"][i][2]<=0:
            contactNE=True
        i+=1 
    i=0
    while i<n and not contactSE:
        if ObjetParNom["supportSE"][i][2]<=0:
            contactSE=True
        i+=1 
    i=0
    while i<n and not contactSW:
        if ObjetParNom["supportSW"][i][2]<=0:
            contactSW=True
        i+=1 
    if (contactNW or contactNE or contactSE or contactSW):
        contact=True
        vitesse[2]=0
    
    
#--------------Initialisation---------------
fig = plt.figure()
ax = Axes3D(fig)
plt.ion()
plt.show()
longueur=20
largeur=10
longueur1Patte=5
longueur2Patte=10
centre=[0,0,30]
NW=[centre[0]-largeur/2,centre[1]+longueur/2,centre[2]]
NE=[centre[0]+largeur/2,centre[1]+longueur/2,centre[2]]
SE=[centre[0]+largeur/2,centre[1]-longueur/2,centre[2]]
SW=[centre[0]-largeur/2,centre[1]-longueur/2,centre[2]]

patte1NW=[NW,np.add(NW,[-longueur1Patte*np.sin(np.pi/4),0,longueur1Patte*np.cos(np.pi/4)])]#1 pour la partie supérieur
patte2NW=[patte1NW[1],np.add(patte1NW[1],[0,0,-longueur2Patte])]#2 pour la partie inférieur

patte1NE=[NE,np.add(NE,[+longueur1Patte*np.sin(np.pi/4),0,longueur1Patte*np.cos(np.pi/4)])]#1 pour la partie supérieur
patte2NE=[patte1NE[1],np.add(patte1NE[1],[0,0,-longueur2Patte])]#2 pour la partie inférieur

patte1SE=[SE,np.add(SE,[+longueur1Patte*np.sin(np.pi/4),0,longueur1Patte*np.cos(np.pi/4)])]#1 pour la partie supérieur
patte2SE=[patte1SE[1],np.add(patte1SE[1],[0,0,-longueur2Patte])]#2 pour la partie inférieur

patte1SW=[SW,np.add(SW,[-longueur1Patte*np.sin(np.pi/4),0,longueur1Patte*np.cos(np.pi/4)])]#1 pour la partie supérieur
patte2SW=[patte1SW[1],np.add(patte1SW[1],[0,0,-longueur2Patte])]#2 pour la partie inférieur

pointsParSupport=15
rayonSupport=2
supportNW=[]
supportNE=[]
supportSE=[]
supportSW=[]
for i in range(pointsParSupport):
    supportNW.append(np.add(patte2NW[1],[rayonSupport*np.cos(np.pi*2*i/pointsParSupport),rayonSupport*np.sin(np.pi*2*i/pointsParSupport),0]))
    supportNE.append(np.add(patte2NE[1],[rayonSupport*np.cos(np.pi*2*i/pointsParSupport),rayonSupport*np.sin(np.pi*2*i/pointsParSupport),0]))
    supportSE.append(np.add(patte2SE[1],[rayonSupport*np.cos(np.pi*2*i/pointsParSupport),rayonSupport*np.sin(np.pi*2*i/pointsParSupport),0]))
    supportSW.append(np.add(patte2SW[1],[rayonSupport*np.cos(np.pi*2*i/pointsParSupport),rayonSupport*np.sin(np.pi*2*i/pointsParSupport),0]))
listeObjets=[[NW,NE,SE,SW],[centre],patte1NW,patte2NW,patte1NE,patte2NE,patte1SE,patte2SE,patte1SW,patte2SW,supportNW,supportNE,supportSE,supportSW]

ObjetParNom={}
ObjetParNom["plateforme"]=listeObjets[0]
ObjetParNom["centre"]=listeObjets[1]
ObjetParNom["patte1NW"]=listeObjets[2]
ObjetParNom["patte2NW"]=listeObjets[3]
ObjetParNom["patte1NE"]=listeObjets[4]
ObjetParNom["patte2NE"]=listeObjets[5]
ObjetParNom["patte1SE"]=listeObjets[6]
ObjetParNom["patte2SE"]=listeObjets[7]
ObjetParNom["patte1SW"]=listeObjets[8]
ObjetParNom["patte2SW"]=listeObjets[9]
ObjetParNom["supportNW"]=listeObjets[10]
ObjetParNom["supportNE"]=listeObjets[11]
ObjetParNom["supportSE"]=listeObjets[12]
ObjetParNom["supportSW"]=listeObjets[13]

ObjetParNom["patte1"]=[ObjetParNom["patte1NW"],ObjetParNom["patte2NW"],ObjetParNom["supportNW"]]
ObjetParNom["patte2"]=[ObjetParNom["patte1NE"],ObjetParNom["patte2NE"],ObjetParNom["supportNE"]]
ObjetParNom["patte3"]=[ObjetParNom["patte1SE"],ObjetParNom["patte2SE"],ObjetParNom["supportSE"]]
ObjetParNom["patte4"]=[ObjetParNom["patte1SW"],ObjetParNom["patte2SW"],ObjetParNom["supportSW"]]


update(listeObjets)

global contactNW,contactNE,contactSE,contactSW,contact
contactNW=False#Permet de vérifier si chaque patte touche le sol ou non
contactNE=False
contactSE=False
contactSW=False
contact=False #permet de vérifier si le robot est en contact avec le sol



dt=0.01#dt intervalle de temps en secondes
global vitesseChute
vitesse=[0,0,0]
g=9.81


NWMotSpeed=[0,0]# vitesse des moteurs pour mvt vertical et horizontal respectivement  en rad.s-1
NEMotSpeed=[0,30]
SEMotSpeed=[0,0]
SWMotSpeed=[0,0]
global motSpeedList
motSpeedList=[NWMotSpeed,NEMotSpeed,SEMotSpeed,SWMotSpeed]

Time(100)
#------------------------------------------

# tests rotation d'une patte:
rotation(ObjetParNom["plateforme"][0],[1,1,0],np.pi/4,[ObjetParNom["patte1NW"],ObjetParNom["patte2NW"],ObjetParNom["supportNW"]])


        
        
        
        
        
        