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
    

def rotation(origi1,vector,w,objetsAPivoter):#w = vites2 de rotation, vector= vecteur directeur de l'axe de rotation
    vector = normalized(vector)
    N=100#effectuer la rotation en N fois permet d'éviter la déformation des pièces à cau2 du calcul en temps discret mais plus long à calculer
    vector=np.multiply(vector,w*dt/N)
    for j in range(len(objetsAPivoter)):
        for m in range(len(objetsAPivoter[j])):#changement de référentiel
            objetsAPivoter[j][m]=np.subtract(objetsAPivoter[j][m],origi1)
        for a in range(N):
            for n in range(len(objetsAPivoter[j])):
                objetsAPivoter[j][n]=np.add(objetsAPivoter[j][n],np.cross(vector,objetsAPivoter[j][n]))
        for p in range(len(objetsAPivoter[j])):#changement de référentiel
            objetsAPivoter[j][p]=objetsAPivoter[j][p]+origi1
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
    ax.autoscale_view(True,True,True,True)
    ax.set_xlim3d(-100,100)
    ax.set_ylim3d(-100,100)
    ax.set_zlim3d(-100,100)
    plt.pau2(0.00000001)
    
def normalized(vector):
    return(vector/np.linalg.norm(vector))
    
def Time(iterations):
    global vites2,motSpeedList
    for i in range(iterations):
        if not contact:
            vites2[2]-=g*dt*100# en cm.s-1
        moveTo(np.multiply(vites2,dt),listeObjets)
        for a in range(4):
            if motSpeedList[a][1]!=0:
                rotation(ObjetParNom["plateforme"][a],[0,0,1],motSpeedList[a][1],ObjetParNom["patte"+str(a)])
            #if motSpeedList[a][0]!=0:
                #vecPatte1=ObjetParNom["Patte"]
        testContact()
        update(listeObjets)
    

def testContact():
    global contact0,contact1,contact2,contact3,contact,vites2
    i=0
    n=len(ObjetParNom["support0"])
    while i<n and not contact0:
        if ObjetParNom["support0"][i][2]<=0:
            contact0=True
        i+=1
    i=0
    while i<n and not contact1:
        if ObjetParNom["support1"][i][2]<=0:
            contact1=True
        i+=1 
    i=0
    while i<n and not contact2:
        if ObjetParNom["support2"][i][2]<=0:
            contact2=True
        i+=1 
    i=0
    while i<n and not contact3:
        if ObjetParNom["support3"][i][2]<=0:
            contact3=True
        i+=1 
    if (contact0 or contact1 or contact2 or contact3):
        contact=True
        vites2[2]=0
    
    
#--------------Initialisation---------------
fig = plt.figure()
ax = Axes3D(fig)
plt.ion()
plt.show()
longueur=20
largeur=10
longueurSupPatte=5
longueurInfPatte=10
centre=[0,0,0]
NW=[centre[0]-largeur/2,centre[1]+longueur/2,centre[2]]
NE=[centre[0]+largeur/2,centre[1]+longueur/2,centre[2]]
SE=[centre[0]+largeur/2,centre[1]-longueur/2,centre[2]]
SW=[centre[0]-largeur/2,centre[1]-longueur/2,centre[2]]

patteSup0=[0,np.add(0,[-longueurSupPatte*np.sin(np.pi/4),0,longueurSupPatte*np.cos(np.pi/4)])]
patteInf0=[patteSup0[1],np.add(patteSup0[1],[0,0,-longueurInfPatte])]

patteSup1=[1,np.add(1,[+longueurSupPatte*np.sin(np.pi/4),0,longueurSupPatte*np.cos(np.pi/4)])]
patteInf1=[patteSup1[1],np.add(patteSup1[1],[0,0,-longueurInfPatte])]

patteSup2=[2,np.add(2,[+longueurSupPatte*np.sin(np.pi/4),0,longueurSupPatte*np.cos(np.pi/4)])]
patteInf2=[patteSup2[1],np.add(patteSup2[1],[0,0,-longueurInfPatte])]

patteSup3=[3,np.add(3,[-longueurSupPatte*np.sin(np.pi/4),0,longueurSupPatte*np.cos(np.pi/4)])]
patteInf3=[patteSup3[1],np.add(patteSup3[1],[0,0,-longueurInfPatte])]

pointsParSupport=15
rayonSupport=2
support0=[]
support1=[]
support2=[]
support3=[]
for i in range(pointsParSupport):
    support0.append(np.add(patteInf0[1],[rayonSupport*np.cos(np.pi*2*i/pointsParSupport),rayonSupport*np.sin(np.pi*2*i/pointsParSupport),0]))
    support1.append(np.add(patteInf1[1],[rayonSupport*np.cos(np.pi*2*i/pointsParSupport),rayonSupport*np.sin(np.pi*2*i/pointsParSupport),0]))
    support2.append(np.add(patteInf2[1],[rayonSupport*np.cos(np.pi*2*i/pointsParSupport),rayonSupport*np.sin(np.pi*2*i/pointsParSupport),0]))
    support3.append(np.add(patteInf3[1],[rayonSupport*np.cos(np.pi*2*i/pointsParSupport),rayonSupport*np.sin(np.pi*2*i/pointsParSupport),0]))
listeObjets=[[0,1,2,3],[centre],patteSup0,patteInf0,patteSup1,patteInf1,patteSup2,patteInf2,patteSup3,patteInf3,support0,support1,support2,support3]

ObjetParNom={}

ObjetParNom["plateforme"]=listeObjets[0]
ObjetParNom["centre"]=listeObjets[1]
ObjetParNom["patteSup0"]=listeObjets[2]
ObjetParNom["patteInf0"]=listeObjets[3]
ObjetParNom["patteSup1"]=listeObjets[4]
ObjetParNom["patteInf1"]=listeObjets[5]
ObjetParNom["patteSup2"]=listeObjets[6]
ObjetParNom["patteInf2"]=listeObjets[7]
ObjetParNom["patteSup3"]=listeObjets[8]
ObjetParNom["patteInf3"]=listeObjets[9]
ObjetParNom["support0"]=listeObjets[10]
ObjetParNom["support1"]=listeObjets[11]
ObjetParNom["support2"]=listeObjets[12]
ObjetParNom["support3"]=listeObjets[13]

ObjetParNom["patte0"]=[ObjetParNom["patteSup0"],ObjetParNom["patteInf0"],ObjetParNom["support0"]]
ObjetParNom["patte1"]=[ObjetParNom["patteSup1"],ObjetParNom["patteInf1"],ObjetParNom["support1"]]
ObjetParNom["patte2"]=[ObjetParNom["patteSup2"],ObjetParNom["patteInf2"],ObjetParNom["support2"]]
ObjetParNom["patte3"]=[ObjetParNom["patteSup3"],ObjetParNom["patteInf3"],ObjetParNom["support3"]]


update(listeObjets)

global contact0,contact1,contact2,contact3,contact
contact0=False#Permet de vérifier si chaque patte touche le sol ou non
contact1=False
contact2=False
contact3=False
contact=False #permet de vérifier si le robot est en contact avec le sol



dt=0.01#dt intervalle de temps en 2condes
global vites2Chute
vites2=[0,0,0]
g=9.81


Mot0Speed=[0,0]# vites2 des moteurs pour mvt vertical et horizontal respectivement  en rad.s-1
Mot1Speed=[0,0]
Mot2Speed=[0,0]
Mot3Speed=[0,0]
Mot0Angle=0
Mot1Angle=0
Mot2Angle=0
Mot3Angle=0

global motSpeedList,motAngleList
motSpeedList=[Mot0Speed,Mot1Speed,Mot2Speed,Mot3Speed]
motAngleList=[Mot0Angle,Mot1Angle,Mot2Angle,Mot3Angle]
#------------------------------------------



        
        
        
        
        
        