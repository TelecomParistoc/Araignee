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
from geometrie import*
from physique import*

def move(vector, ObjetsABouger):
    for i in range(len(ObjetsABouger)):
        for j in range(len(ObjetsABouger[i])):
            ObjetsABouger[i][j]=np.add(ObjetsABouger[i][j], vector)
    # update(listeObjets)


def rotation(origine, vector, w, objetsAPivoter): # w = vitesse de rotation, vector= vecteur directeur de l'axe de rotation
    vector = normalized(vector)
    vector=np.multiply(vector, w*dt)
    for j in range(len(objetsAPivoter)):
        for m in range(len(objetsAPivoter[j])):#changement de référentiel
            objetsAPivoter[j][m]=np.subtract(objetsAPivoter[j][m], origine)
        for n in range(len(objetsAPivoter[j])):#on decompose la rotation en 3 rotations
            Rot=np.array([[1,0,0], [0,np.cos(vector[0]),np.sin(vector[0])], [0,-np.sin(vector[0]),np.cos(vector[0])]]) # matrice de rotation dans le plan y,z
            objetsAPivoter[j][n]=np.dot(Rot,objetsAPivoter[j][n])
            Rot=np.array([[np.cos(vector[1]), 0, -np.sin(vector[1])],[0,1,0], [np.sin(vector[1]), 0, np.cos(vector[1])]]) # matrice de rotation dans le plan z,x
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
    ax.set_xlim3d(-axlim,axlim)
    ax.set_ylim3d(-axlim,axlim)
    ax.set_zlim3d(-axlim,axlim)
    plt.pause(0.00000001)
<<<<<<< HEAD
    
    
=======


>>>>>>> origin/test_felix
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
                    vecPatteInf=np.subtract(ObjetParNom["patte"+str(a)+"Inf2"][1],ObjetParNom["patte"+str(a)+"Inf2"][0])
                    vecNormal=np.cross(vecPatteInf,[0,0,1])
                    rotation(ObjetParNom["fixationSup"+str(a)][0],vecNormal,-motSpeedList[a][0],[ObjetParNom["patte"+str(a)+"Sup1"]])
                    rotation(ObjetParNom["fixationInf"+str(a)][0],vecNormal,-motSpeedList[a][0],[ObjetParNom["patte"+str(a)+"Sup2"]])
                    ObjetParNom["patte"+str(a)+"Inf1"][0]=ObjetParNom["patte"+str(a)+"Sup1"][1]
                    ObjetParNom["patte"+str(a)+"Inf1"][1]=ObjetParNom["patte"+str(a)+"Sup2"][1]
                    move(np.subtract(ObjetParNom["patte"+str(a)+"Sup2"][1],ObjetParNom["patte"+str(a)+"Inf2"][0]),[ObjetParNom["patte"+str(a)+"Inf2"],ObjetParNom["support"+str(a)]])
                    motAngleList[a][0]+=motSpeedList[a][0]*dt
                    testPosMot(a,0)
            else:
                if motSpeedList[a][1]!=0:
                    rotation(ObjetParNom["fixationInf"+str(a)][0],[0,0,1],-motSpeedList[a][1],[ObjetParNom["fixationSup"+str(a)]]+ObjetParNom["patte"+str(a)])
                    motAngleList[a][1]+=motSpeedList[a][1]*dt
                    testPosMot(a,1)
                if motSpeedList[a][0]!=0:
                    vecPatteInf=np.subtract(ObjetParNom["patte"+str(a)+"Inf2"][1],ObjetParNom["patte"+str(a)+"Inf2"][0])
                    vecNormal=np.cross(vecPatteInf,[0,0,1])
                    rotation(ObjetParNom["fixationSup"+str(a)][0],vecNormal,-motSpeedList[a][0],[ObjetParNom["patte"+str(a)+"Sup1"]])
                    rotation(ObjetParNom["fixationInf"+str(a)][0],vecNormal,-motSpeedList[a][0],[ObjetParNom["patte"+str(a)+"Sup2"]])
                    ObjetParNom["patte"+str(a)+"Inf1"][0]=ObjetParNom["patte"+str(a)+"Sup1"][1]
                    ObjetParNom["patte"+str(a)+"Inf1"][1]=ObjetParNom["patte"+str(a)+"Sup2"][1]
                    move(np.subtract(ObjetParNom["patte"+str(a)+"Sup2"][1],ObjetParNom["patte"+str(a)+"Inf2"][0]),[ObjetParNom["patte"+str(a)+"Inf2"],ObjetParNom["support"+str(a)]])
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
    if motAngleList[a][i]>motAngleLim[i][0]-motAngleList[a][i]*dt or motAngleList[a][i]<motAngleLim[i][1]+motAngleList[a][i]*dt:#limite avec marge d'erreur car calcul temps discret
        motSpeedList[a][i]*=-1
<<<<<<< HEAD
        

def momentInertie(listePoints,origine,vector):#listePoints : liste de [coordonnées,masse]
    J=0
    #for point in listePoints:
        #J+=point[1]*(distanceDroitePoint(point[0],origine,vector))**2
    #return (J)

def rotTriangle(triangle,point):# see ray casting algorithm
    vecTest=[0,1]#direction choisie arbitrairement
    count=0
    listeVecteurs=[[triangle[0],triangle[1]],[triangle[1],triangle[2]],[triangle[2],triangle[0]]]
    for vecteur in listeVecteurs :
        if vecteur[1][1]>vecteur[0][1]:
            A=[vecteur[0][0],vecteur[0][1]]
            B=[vecteur[1][0],vecteur[1][1]]
        else:
            A=[vecteur[1][0],vecteur[1][1]]
            B=[vecteur[0][0],vecteur[0][1]]
        if max(vecteur[0][0],vecteur[1][0])>point[0] and min(vecteur[0][0],vecteur[1][0])<point[0]:
            if A[1]>point[1] :
                count+=1
            if B[1]>point[1] :
                if A[0]!=B[0]:
                    pente1=abs((B[1]-A[1])/(B[0]-A[0]))
                    pente2=abs((point[1]-A[1])/(point[0]-A[0]))
                    if pente2<pente1 :
                        count+=1
    if count%2==1:
        return [True,None,None]
    else :
        normaux=[]
        normaux.append([projeteOrtho(triangle[2],triangle[0],np.subtract(triangle[1],triangle[0]))])#vecteur normal au 1ersegment
        normaux.append([projeteOrtho(triangle[0],triangle[1],np.subtract(triangle[2],triangle[1]))])#vecteur normal au second segment
        normaux.append([projeteOrtho(triangle[1],triangle[2],np.subtract(triangle[0],triangle[2]))])#vecteur normal au troisième segment
        
        vec1=np.cross(normaux[0],np.subtract(point,triangle[1]))
        vec2=np.cross(normaux[1],np.subtract(point,triangle[1]))
        if np.dot(vec1,vec2)<0:
            return [False,listeVecteurs[2]]
            
        vec1=np.cross(normaux[1],np.subtract(point,triangle[2]))
        vec2=np.cross(normaux[2],np.subtract(point,triangle[2]))
        
        if np.dot(vec1,vec2)<0:
            return [False,listeVecteurs[0]]
            
        vec1=np.cross(normaux[2],np.subtract(point,triangle[0]))
        vec2=np.cross(normaux[0],np.subtract(point,triangle[0]))
        return [False,listeVecteurs[1]]
            
=======
    
#TODO faire une fonction qui donne les couples des moteurs en fonction des vitesses
# à déterminer par une modélisation empirique. Rappel : P = C * omega

#TODO choisir parmi les possibilités suivantes :
# - pas de glissement, éliminer les rotations incompatibles
# - pas de glissement, imposer une contrainte sur la plateforme, quand on le teste
# le modifier immédiatement
# - glissement, avec des frottements...

#TODO comment déterminer le moment cinétique ?
# on peut se contenter de calculer uniquement le moment cinétique de la plateforme
# (modélisée par 4 points ? + la batterie)

#TODO fonction pour faire basculer le robot

#TODO tester les nouvelles fonctions




    
>>>>>>> origin/test_felix
#--------------Initialisation---------------
fig = plt.figure()
ax = Axes3D(fig)
plt.ion()
plt.show()

axlim=100

longueur=15
largeur=10
longueurSupPatte=5
longueurInfPatte=10

longueurSup1Patte=9
longueurSup2Patte=9
longueurInf1Patte=3#pas utilisé dans cette version car fixée par les autres morceaux
longueurInf2Patte=9
angleInfPatte=0.157
centre=[0,0,0]
NW=[centre[0]-largeur/2,centre[1]+longueur/2,centre[2]]
NE=[centre[0]+largeur/2,centre[1]+longueur/2,centre[2]]
SE=[centre[0]+largeur/2,centre[1]-longueur/2,centre[2]]
SW=[centre[0]-largeur/2,centre[1]-longueur/2,centre[2]]

fixationSupNW=np.add(NW,[+1/2,0,3])
fixationSupNE=np.add(NE,[-1/2,0,3])
fixationSupSE=np.add(SE,[-1/2,0,3])
fixationSupSW=np.add(SW,[+1/2,0,3])

fixationInfNW=np.add(NW,[-1/2,0,1])
fixationInfNE=np.add(NE,[+1/2,0,1])
fixationInfSE=np.add(SE,[+1/2,0,1])
fixationInfSW=np.add(SW,[-1/2,0,1])

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



mot0Speed=[-30,30]# vitesse des moteurs pour mvt vertical et horizontal respectivement  en rad.s-1
mot1Speed=[-30,30]
mot2Speed=[-30,30]#[0]>0 --> patte vers le haut // [1]>0 --> patte vers l'avant
mot3Speed=[-30,30]

mot0Angle=[0,0]
mot1Angle=[0,0]
mot2Angle=[0,0]
mot3Angle=[0,0]


global motSpeedList,motAngleList,motAngleLim
motAngleLim=[[3.14/2,-3.14/4],[3.14/3,-3.14/3]]#[[max,min],[max,min]] 
motSpeedList=[mot0Speed,mot1Speed,mot2Speed,mot3Speed]
motAngleList=[mot0Angle,mot1Angle,mot2Angle,mot3Angle]


Time(150)

#------------------------------------------



        
        
        
        
        
        