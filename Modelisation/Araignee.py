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

def move(vector,ObjetsABouger):
    for i in range(len(ObjetsABouger)):
        for j in range(len(ObjetsABouger[i])):
            ObjetsABouger[i][j]=np.add(ObjetsABouger[i][j],vector)
    #update(listeObjets)

def rotation(origine,vector,w,objetsAPivoter):#w = vitesse de rotation, vector= vecteur directeur de l'axe de rotation
    vector = normalized(vector)
    vector=np.multiply(vector,w*dt)
    for j in range(len(objetsAPivoter)):
        for m in range(len(objetsAPivoter[j])):#changement de référentiel
            objetsAPivoter[j][m]=np.subtract(objetsAPivoter[j][m],origine)
        for n in range(len(objetsAPivoter[j])):#on decompose la rotation en 3 rotations
            Rot=np.array([[1,0,0],[0,np.cos(vector[0]),np.sin(vector[0])],[0,-np.sin(vector[0]),np.cos(vector[0])]])#matrice de rotation dans le plan y,z
            objetsAPivoter[j][n]=np.dot(Rot,objetsAPivoter[j][n])
            Rot=np.array([[np.cos(vector[1]),0,-np.sin(vector[1])],[0,1,0],[np.sin(vector[1]),0,np.cos(vector[1])]])#matrice de rotation dans le plan z,x
            objetsAPivoter[j][n]=np.dot(Rot,objetsAPivoter[j][n])
            Rot=np.array([[np.cos(vector[2]),np.sin(vector[2]),0],[-np.sin(vector[2]),np.cos(vector[2]),0],[0,0,1]])#matrice de rotation dans le plan x,y
            objetsAPivoter[j][n]=np.dot(Rot,objetsAPivoter[j][n])
        for p in range(len(objetsAPivoter[j])):#changement de référentiel inverse
            objetsAPivoter[j][p]=objetsAPivoter[j][p]+origine
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
    plt.pause(0.00000001)
    
def normalized(vector):
    return(vector/np.linalg.norm(vector))
    
def Time(iterations):
    global vitesse,motSpeedList,motAngleList
    for i in range(iterations):
        if not contact:
            vitesse[2]-=g*dt*100# en cm.s-1
        move(np.multiply(vitesse,dt),listeObjets)
        for a in range(4):
            if a==0 or a==3:
                if motSpeedList[a][1]!=0:
                    rotation(ObjetParNom["fixationInf"+str(a)][0],[0,0,1],motSpeedList[a][1],[ObjetParNom["fixationSup"+str(a)]]+ObjetParNom["patte"+str(a)])
                    motAngleList[a][1]+=motSpeedList[a][1]*dt
                    testPosMot(a,1)
                if motSpeedList[a][0]!=0:
                    vecPatteSup=np.subtract(ObjetParNom["patte"+str(a)+"Sup1"][1],ObjetParNom["patte"+str(a)+"Sup1"][0])
                    vecPatteInf=np.subtract(ObjetParNom["patte"+str(a)+"Inf2"][1],ObjetParNom["patte"+str(a)+"Inf2"][0])
                    vecNormal=np.cross(vecPatteInf,vecPatteSup)
                    rotation(ObjetParNom["fixationSup"+str(a)][0],vecNormal,-motSpeedList[a][0],ObjetParNom["patte"+str(a)])
                    motAngleList[a][0]+=motSpeedList[a][0]*dt
                    testPosMot(a,0)
            else:
                if motSpeedList[a][1]!=0:
                    rotation(ObjetParNom["fixationInf"+str(a)][0],[0,0,1],-motSpeedList[a][1],[ObjetParNom["fixationSup"+str(a)]]+ObjetParNom["patte"+str(a)])
                    motAngleList[a][1]+=motSpeedList[a][1]*dt
                    testPosMot(a,1)
                if motSpeedList[a][0]!=0:
                    vecPatteSup=np.subtract(ObjetParNom["patte"+str(a)+"Sup1"][1],ObjetParNom["patte"+str(a)+"Sup1"][0])
                    vecPatteInf=np.subtract(ObjetParNom["patte"+str(a)+"Inf2"][1],ObjetParNom["patte"+str(a)+"Inf2"][0])
                    vecNormal=np.cross(vecPatteInf,vecPatteSup)
                    rotation(ObjetParNom["fixationSup"+str(a)][0],vecNormal,-motSpeedList[a][0],ObjetParNom["patte"+str(a)])
                    motAngleList[a][0]+=motSpeedList[a][0]*dt
                    testPosMot(a,0)
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
        vitesse[2]=0

def testPosMot(a,i):
    global motAngleList,motAngleLim
    if motAngleList[a][i]>=motAngleLim[i][0] or motAngleList[a][i]<=motAngleLim[i][1]:
        motSpeedList[a][i]*=-1
    

    # commentaire bidon
    
#--------------Initialisation---------------
fig = plt.figure()
ax = Axes3D(fig)
plt.ion()
plt.show()
longueur=15
largeur=10
longueurSupPatte=5
longueurInfPatte=10

longueurSup1Patte=9
longueurSup2Patte=9
longueurInf1Patte=3#pas utilisé dans cette version car fixée par les autres morceaux
longueurInf2Patte=9
angleInfPatte=0.157
centre=[0,0,100]
NW=[centre[0]-largeur/2,centre[1]+longueur/2,centre[2]]
NE=[centre[0]+largeur/2,centre[1]+longueur/2,centre[2]]
SE=[centre[0]+largeur/2,centre[1]-longueur/2,centre[2]]
SW=[centre[0]-largeur/2,centre[1]-longueur/2,centre[2]]

fixationSupNW=np.add(NW,[+1,0,3])
fixationSupNE=np.add(NE,[-1,0,3])
fixationSupSE=np.add(SE,[-1,0,3])
fixationSupSW=np.add(SW,[+1,0,3])

fixationInfNW=np.add(NW,[-1,0,1])
fixationInfNE=np.add(NE,[+1,0,1])
fixationInfSE=np.add(SE,[+1,0,1])
fixationInfSW=np.add(SW,[-1,0,1])

patte0Sup1=[fixationSupNW,np.add(fixationSupNW,[-longueurSup1Patte,0,0])]
patte0Sup2=[fixationInfNW,np.add(fixationInfNW,[-longueurSup2Patte,0,0])]
patte0Inf1=[patte0Sup1[1],patte0Sup2[1]]
patte0Inf2=[patte0Inf1[1],np.add(patte0Inf1[1],[-np.sin(angleInfPatte)*longueurInf2Patte,0,-np.cos(angleInfPatte)*longueurInf2Patte])]


patte1Sup1=[fixationSupNE,np.add(fixationSupNE,[+longueurSup1Patte,0,0])]
patte1Sup2=[fixationInfNE,np.add(fixationInfNE,[+longueurSup2Patte,0,0])]
patte1Inf1=[patte1Sup1[1],patte1Sup2[1]]
patte1Inf2=[patte1Inf1[1],np.add(patte1Inf1[1],[+np.sin(angleInfPatte)*longueurInf2Patte,0,-np.cos(angleInfPatte)*longueurInf2Patte])]

patte2Sup1=[fixationSupSE,np.add(fixationSupSE,[+longueurSup1Patte,0,0])]
patte2Sup2=[fixationInfSE,np.add(fixationInfSE,[+longueurSup2Patte,0,0])]
patte2Inf1=[patte2Sup1[1],patte2Sup2[1]]
patte2Inf2=[patte2Inf1[1],np.add(patte2Inf1[1],[+np.sin(angleInfPatte)*longueurInf2Patte,0,-np.cos(angleInfPatte)*longueurInf2Patte])]

patte3Sup1=[fixationSupSW,np.add(fixationSupSW,[-longueurSup1Patte,0,0])]
patte3Sup2=[fixationInfSW,np.add(fixationInfSW,[-longueurSup2Patte,0,0])]
patte3Inf1=[patte3Sup1[1],patte3Sup2[1]]
patte3Inf2=[patte3Inf1[1],np.add(patte3Inf1[1],[-np.sin(angleInfPatte)*longueurInf2Patte,0,-np.cos(angleInfPatte)*longueurInf2Patte])]

pointsParSupport=15
rayonSupport=2
support0=[]
support1=[]
support2=[]
support3=[]
for i in range(pointsParSupport):
    support0.append(np.add(patte0Inf2[1],[rayonSupport*np.cos(np.pi*2*i/pointsParSupport),rayonSupport*np.sin(np.pi*2*i/pointsParSupport),0]))
    support1.append(np.add(patte1Inf2[1],[rayonSupport*np.cos(np.pi*2*i/pointsParSupport),rayonSupport*np.sin(np.pi*2*i/pointsParSupport),0]))
    support2.append(np.add(patte2Inf2[1],[rayonSupport*np.cos(np.pi*2*i/pointsParSupport),rayonSupport*np.sin(np.pi*2*i/pointsParSupport),0]))
    support3.append(np.add(patte3Inf2[1],[rayonSupport*np.cos(np.pi*2*i/pointsParSupport),rayonSupport*np.sin(np.pi*2*i/pointsParSupport),0]))
listeObjets=[[NW,NE,SE,SW],[centre],patte0Sup1,patte0Sup2,patte0Inf1,patte0Inf2,patte1Sup1,patte1Sup2,patte1Inf1,patte1Inf2,patte2Sup1,patte2Sup2,patte2Inf1,patte2Inf2,patte3Sup1,patte3Sup2,patte3Inf1,patte3Inf2,support0,support1,support2,support3,[fixationInfNW],[fixationInfNE],[fixationInfSE],[fixationInfSW],[fixationSupNW],[fixationSupNE],[fixationSupSE],[fixationSupSW]]


ObjetParNom={}

ObjetParNom["araignee"]=listeObjets
ObjetParNom["plateforme"]=listeObjets[0]
ObjetParNom["centre"]=listeObjets[1]
ObjetParNom["patte0Sup1"]=listeObjets[2]
ObjetParNom["patte0Sup2"]=listeObjets[3]
ObjetParNom["patte0Inf1"]=listeObjets[4]
ObjetParNom["patte0Inf2"]=listeObjets[5]
ObjetParNom["patte1Sup1"]=listeObjets[6]
ObjetParNom["patte1Sup2"]=listeObjets[7]
ObjetParNom["patte1Inf1"]=listeObjets[8]
ObjetParNom["patte1Inf2"]=listeObjets[9]
ObjetParNom["patte2Sup1"]=listeObjets[10]
ObjetParNom["patte2Sup2"]=listeObjets[11]
ObjetParNom["patte2Inf1"]=listeObjets[12]
ObjetParNom["patte2Inf2"]=listeObjets[13]
ObjetParNom["patte3Sup1"]=listeObjets[14]
ObjetParNom["patte3Sup2"]=listeObjets[15]
ObjetParNom["patte3Inf1"]=listeObjets[16]
ObjetParNom["patte3Inf2"]=listeObjets[17]
ObjetParNom["support0"]=listeObjets[18]
ObjetParNom["support1"]=listeObjets[19]
ObjetParNom["support2"]=listeObjets[20]
ObjetParNom["support3"]=listeObjets[21]
ObjetParNom["fixationInf0"]=listeObjets[22]
ObjetParNom["fixationInf1"]=listeObjets[23]
ObjetParNom["fixationInf2"]=listeObjets[24]
ObjetParNom["fixationInf3"]=listeObjets[25]
ObjetParNom["fixationSup0"]=listeObjets[26]
ObjetParNom["fixationSup1"]=listeObjets[27]
ObjetParNom["fixationSup2"]=listeObjets[28]
ObjetParNom["fixationSup3"]=listeObjets[29]



ObjetParNom["patte0"]=[ObjetParNom["patte0Sup1"],ObjetParNom["patte0Sup2"],ObjetParNom["patte0Inf1"],ObjetParNom["patte0Inf2"],ObjetParNom["support0"]]
ObjetParNom["patte1"]=[ObjetParNom["patte1Sup1"],ObjetParNom["patte1Sup2"],ObjetParNom["patte1Inf1"],ObjetParNom["patte1Inf2"],ObjetParNom["support1"]]
ObjetParNom["patte2"]=[ObjetParNom["patte2Sup1"],ObjetParNom["patte2Sup2"],ObjetParNom["patte2Inf1"],ObjetParNom["patte2Inf2"],ObjetParNom["support2"]]
ObjetParNom["patte3"]=[ObjetParNom["patte3Sup1"],ObjetParNom["patte3Sup2"],ObjetParNom["patte3Inf1"],ObjetParNom["patte3Inf2"],ObjetParNom["support3"]]


update(listeObjets)

global contact0,contact1,contact2,contact3,contact
contact0=False#Permet de vérifier si chaque patte touche le sol ou non
contact1=False
contact2=False
contact3=False
contact=False #permet de vérifier si le robot est en contact avec le sol



dt=0.01#dt intervalle de temps en secondes
global vitesse
vitesse=[0,0,0]
g=9.81



mot0Speed=[30,0]# vitesse des moteurs pour mvt vertical et horizontal respectivement  en rad.s-1
mot1Speed=[30,0]
mot2Speed=[0,30]#[0]>0 --> patte vers le haut // [1]>0 --> patte vers l'avant
mot3Speed=[0,30]

mot0Angle=[0,0]
mot1Angle=[0,0]
mot2Angle=[0,0]
mot3Angle=[0,0]


global motSpeedList,motAngleList,motAngleLim
motAngleLim=[[3.14/2,-3.14/4],[3.14/4,-3.14/2]]#[[max,min],[max,min]] 
motSpeedList=[mot0Speed,mot1Speed,mot2Speed,mot3Speed]
motAngleList=[mot0Angle,mot1Angle,mot2Angle,mot3Angle]


Time(100)

#------------------------------------------



        
        
        
        
        
        