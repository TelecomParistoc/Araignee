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

def normalized(vector):
    return(vector/np.linalg.norm(vector))


def Time(iterations):
    global vitesse,motSpeedList,motAngleList, contact, contactList
    for i in range(iterations):
        print(i)
        if not contact:
            vitesse[2]-=g*dt*100# en cm.s-1
            move(np.multiply(vitesse,dt),listeObjets)
        for a in range(4):
            if not contactList[a]:
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
            else:

                if a==0 or a==3:
                    if motSpeedList[a][1]!=0:
                        rotation(ObjetParNom["patte"+str(a)+"Inf2"][1],[0,0,1],+motSpeedList[a][1],[ObjetParNom["fixationSup"+str(a)],ObjetParNom["fixationInf"+str(a)]]+ObjetParNom["patte"+str(a)])
                        motAngleList[a][1]+=motSpeedList[a][1]*dt
                        testPosMot(a,1)
                    if motSpeedList[a][0]>0:
                        vecPatteInf=np.subtract(ObjetParNom["patte"+str(a)+"Inf2"][1],ObjetParNom["patte"+str(a)+"Inf2"][0])
                        vecNormal=np.cross(vecPatteInf,[0,0,1])
                        rotation(ObjetParNom["fixationSup"+str(a)][0],vecNormal,-motSpeedList[a][0],[ObjetParNom["patte"+str(a)+"Sup1"]])
                        rotation(ObjetParNom["fixationInf"+str(a)][0],vecNormal,-motSpeedList[a][0],[ObjetParNom["patte"+str(a)+"Sup2"]])
                        ObjetParNom["patte"+str(a)+"Inf1"][0]=ObjetParNom["patte"+str(a)+"Sup1"][1]
                        ObjetParNom["patte"+str(a)+"Inf1"][1]=ObjetParNom["patte"+str(a)+"Sup2"][1]
                        move(np.subtract(ObjetParNom["patte"+str(a)+"Sup2"][1],ObjetParNom["patte"+str(a)+"Inf2"][0]),[ObjetParNom["patte"+str(a)+"Inf2"],ObjetParNom["support"+str(a)]])
                        motAngleList[a][0]+=motSpeedList[a][0]*dt
                        testPosMot(a,0)
                    elif motSpeedList[a][0]<0:
                        vecPatteInf=np.subtract(ObjetParNom["patte"+str(a)+"Inf2"][1],ObjetParNom["patte"+str(a)+"Inf2"][0])
                        vecNormal=np.cross(vecPatteInf,[0,0,1])
                        rotation(ObjetParNom["fixationSup"+str(a)][0],vecNormal,-motSpeedList[a][0],[ObjetParNom["patte"+str(a)+"Sup1"]])
                        rotation(ObjetParNom["fixationInf"+str(a)][0],vecNormal,-motSpeedList[a][0],[ObjetParNom["patte"+str(a)+"Sup2"]])
                        ObjetParNom["patte"+str(a)+"Inf1"][0]=ObjetParNom["patte"+str(a)+"Sup1"][1]
                        ObjetParNom["patte"+str(a)+"Inf1"][1]=ObjetParNom["patte"+str(a)+"Sup2"][1]
                        move(np.subtract(ObjetParNom["patte"+str(a)+"Sup2"][1],ObjetParNom["patte"+str(a)+"Inf2"][0]),[ObjetParNom["patte"+str(a)+"Inf2"],ObjetParNom["support"+str(a)]])
                        motAngleList[a][0]+=motSpeedList[a][0]*dt
                        testPosMot(a,0)
                        move([0,0,-ObjetParNom["patte"+str(a)+"Inf2"][1][2]-0.01],[ObjetParNom["fixationSup"+str(a)],ObjetParNom["fixationInf"+str(a)]]+ObjetParNom["patte"+str(a)])

                else:
                    if motSpeedList[a][1]!=0:
                        rotation(ObjetParNom["patte"+str(a)+"Inf2"][1],[0,0,1],-motSpeedList[a][1],[ObjetParNom["fixationSup"+str(a)],ObjetParNom["fixationInf"+str(a)]]+ObjetParNom["patte"+str(a)])
                        motAngleList[a][1]+=motSpeedList[a][1]*dt
                        testPosMot(a,1)
                    if motSpeedList[a][0]>0:
                        vecPatteInf=np.subtract(ObjetParNom["patte"+str(a)+"Inf2"][1],ObjetParNom["patte"+str(a)+"Inf2"][0])
                        vecNormal=np.cross(vecPatteInf,[0,0,1])
                        rotation(ObjetParNom["fixationSup"+str(a)][0],vecNormal,-motSpeedList[a][0],[ObjetParNom["patte"+str(a)+"Sup1"]])
                        rotation(ObjetParNom["fixationInf"+str(a)][0],vecNormal,-motSpeedList[a][0],[ObjetParNom["patte"+str(a)+"Sup2"]])
                        ObjetParNom["patte"+str(a)+"Inf1"][0]=ObjetParNom["patte"+str(a)+"Sup1"][1]
                        ObjetParNom["patte"+str(a)+"Inf1"][1]=ObjetParNom["patte"+str(a)+"Sup2"][1]
                        move(np.subtract(ObjetParNom["patte"+str(a)+"Sup2"][1],ObjetParNom["patte"+str(a)+"Inf2"][0]),[ObjetParNom["patte"+str(a)+"Inf2"],ObjetParNom["support"+str(a)]])
                        motAngleList[a][0]+=motSpeedList[a][0]*dt
                        testPosMot(a,0)
                    elif motSpeedList[a][0]<0:
                        vecPatteInf=np.subtract(ObjetParNom["patte"+str(a)+"Inf2"][1],ObjetParNom["patte"+str(a)+"Inf2"][0])
                        vecNormal=np.cross(vecPatteInf,[0,0,1])
                        rotation(ObjetParNom["fixationSup"+str(a)][0],vecNormal,-motSpeedList[a][0],[ObjetParNom["patte"+str(a)+"Sup1"]])
                        rotation(ObjetParNom["fixationInf"+str(a)][0],vecNormal,-motSpeedList[a][0],[ObjetParNom["patte"+str(a)+"Sup2"]])
                        ObjetParNom["patte"+str(a)+"Inf1"][0]=ObjetParNom["patte"+str(a)+"Sup1"][1]
                        ObjetParNom["patte"+str(a)+"Inf1"][1]=ObjetParNom["patte"+str(a)+"Sup2"][1]
                        move(np.subtract(ObjetParNom["patte"+str(a)+"Sup2"][1],ObjetParNom["patte"+str(a)+"Inf2"][0]),[ObjetParNom["patte"+str(a)+"Inf2"],ObjetParNom["support"+str(a)]])
                        motAngleList[a][0]+=motSpeedList[a][0]*dt
                        testPosMot(a,0)
                        move([0,0,-ObjetParNom["patte"+str(a)+"Inf2"][1][2]-0.01],[ObjetParNom["fixationSup"+str(a)],ObjetParNom["fixationInf"+str(a)]]+ObjetParNom["patte"+str(a)])

        if contact:#respect des dimensions forcé


            # TODO traiter les mouvements liés à l'inertie du robot

            u=[0.0,0.0,0.0]
            for i in range(4):
                u[0]+=ObjetParNom["fixationInf"+str(i)][0][0]
                u[1]+=ObjetParNom["fixationInf"+str(i)][0][1]
                u[2]+=ObjetParNom["fixationInf"+str(i)][0][2]
            u=np.multiply(u,0.25)
            u[2]-=1 # TODO régler le problème des pattes en biais
            vec=np.subtract(u,ObjetParNom["centre"])[0]
            move(vec,[ObjetParNom["plateforme"],ObjetParNom["centre"]])
            vitesse=np.multiply(vec,1.0/dt)
            print("deform",listeDeformationPattes())    
            """
            listeDef=listeDeformationPattes()
            listeContacts=listePatteContact()
            defMaxInd=0
            for i in range(4):
                if i in listeContacts:
                    if abs(listeDef[i])>abs(listeDef[defMaxInd]):
                        defMaxInd=i
            if listeDef[defMaxInd]>0:
                oppose=(defMaxInd+2)%4
                d=listeDef[defMaxInd]-listeDef[oppose]
                d=d*0.5
                delta=abs(ObjetParNom["centre"][0][2]-ObjetParNom["plateforme"][defMaxInd][2])
                theta=np.arcsin(delta/(np.sqrt(longueur**2+largeur**2)*0.5))
                alpha=np.arctan((abs(delta-d)/(np.cos(theta)*np.sqrt(longueur**2+largeur**2)*0.5)))
                angle=abs(theta-alpha)
                print("angle",angle)
                u=np.subtract(ObjetParNom["plateforme"][defMaxInd],ObjetParNom["centre"])
                v=np.add(u,[0,0,1])
                vector=np.cross(u,v)
                print(u,v)
                print("vector",vector)
                rotation(ObjetParNom["patte"+str(oppose)+"Inf2"][1], vector[0], -angle/dt, listeObjets)

            elif listeDef[defMaxInd]<0:
                oppose=(defMaxInd+2)%4
                d=listeDef[defMaxInd]-listeDef[oppose]
                d=d*0.5
                theta=np.arcsin(delta/(np.sqrt(longueur**2+largeur**2)*0.5))
                alpha=np.arctan((abs(delta-d)/(np.cos(theta)*np.sqrt(longueur**2+largeur**2)*0.5)))
                angle=abs(theta-alpha)
                print("angle",angle)
                u=np.subtract(ObjetParNom["plateforme"][defMaxInd],ObjetParNom["centre"])
                v=np.add(u,[0,0,1])
                print(u,v)
                vector=np.cross(u,v)
                print("vector",vector)
                rotation(ObjetParNom["patte"+str(defMaxInd)+"Inf2"][1], vector[0], angle/dt, listeObjets)
                """
                
            for i in range(4):
                u=[0.0,0.0,-1.0]
                u[0]+=ObjetParNom["fixationInf"+str(i)][0][0]
                u[1]+=ObjetParNom["fixationInf"+str(i)][0][1]
                u[2]+=ObjetParNom["fixationInf"+str(i)][0][2]
                if(i==0 or i==3):
                    u[0]+=0.5
                else:
                    u[0]-=0.5
                move(np.subtract(ObjetParNom["plateforme"][i],u),ObjetParNom["patte"+str(i)]+[ObjetParNom["fixationInf"+str(i)],ObjetParNom["fixationSup"+str(i)]])
                
                
        
        testContact()
        update(listeObjets)
        print("0",listeDeformationPattes())

def listePatteContact():
    l=[]
    for i in range(4):
        if contactList[i]:
            l.append(i)

    return(l)

def listeDeformationPattes():
    L=[]
    for i in range(4):
        deformation=ObjetParNom["fixationInf"+str(i)][0][2]-(ObjetParNom["plateforme"][i][2]+1)
        L.append(deformation)
    return(L)

"""
def testContact():
    global vitesse,contact,contactList
    i=0
    n=len(ObjetParNom["support0"])
    contactList=[False,False,False,False]
    contact=False
    while i<n and not contactList[0]:
        if ObjetParNom["support0"][i][2]<=0:
            contactList[0]=True
        i+=1
    i=0
    while i<n and not contactList[1]:
        if ObjetParNom["support1"][i][2]<=0:
            contactList[1]=True
        i+=1
    i=0
    while i<n and not contactList[2]:
        if ObjetParNom["support2"][i][2]<=0:
            contactList[2]=True
        i+=1
    i=0
    while i<n and not contactList[3]:
        if ObjetParNom["support3"][i][2]<=0:
            contactList[3]=True
        i+=1
    if (contactList[0] or contactList[1] or contactList[2] or contactList[3]):
        contact=True
        if vitesse[2]<0:
            vitesse[2]=0
"""


def posPieds():
    """fonction qui renvoie une liste avec la position des pieds"""
    global ObjetParNom, contactList

    listePieds = []
    for i in range(4):
        if contactList[i]:
            listePieds += [[i, ObjetParNom["patte"+str(i)+"Inf2"][1][0:2]]]
    return listePieds


def testContact():
    global vitesse,contact,contactList
    contactList=[False,False,False,False]
    contact=False
    for a in range(4):
        if ObjetParNom["patte"+str(a)+"Inf2"][1][2]<=0:
            contactList[a]=True
    if (contactList[0] or contactList[1] or contactList[2] or contactList[3]):
        contact=True
        if vitesse[2]<0:
            vitesse[2]=0



def testPosMot(a,i):
    global motAngleList,motAngleLim
    if motAngleList[a][i]>motAngleLim[i][0]-abs(motSpeedList[a][i]*dt) or motAngleList[a][i]<motAngleLim[i][1]+abs(motSpeedList[a][i]*dt):#limite avec marge d'erreur car calcul temps discret
        motSpeedList[a][i]*=-1


def getMasses():
    """fonction qui renvoie une liste avec les coordonnées des quatre
    moteurs associés à leur masse"""
    global masseMoteur

    listePoints = []
    # TODO modifier quand ça ira
    for i in range(4):
        listePoints += [[ObjetParNom["plateforme"][i], 2*masseMoteur]]

    return listePoints


# TODO vérifier que la fonction marche
def updateRot(centreGravite, dt):
    """fonction qui met à jour la liste listeRotation contenant l'axe'
    et la vitesse angulaire"""

    global listeRotation
    testContact()
    listePieds = posPieds()
    ref1, ref2 = axeRotation(listePieds, centreGravite)
    if ref1 is None:
        listeRotation = []
    elif listeRotation == []:
        listeRotation = [ref1, ref2, 0]
    else:
        if ref1 == listeRotation[0] and ref2 == listeRotation[1]:
            omega = listeRotation[2]
            origine = ObjetParNom["patte"+str(ref1)+"Inf2"][1]
            point = ObjetParNom["patte"+str(ref2)+"Inf2"][1]
            vecteur = np.subtract(origine, point)
            mom_poids = moment_poids(getMasses(), origine, vecteur, 9.81)
            mom_inertie = momentInertie(getMasses(), origine, vecteur)
            omega += (mom_poids/mom_inertie)*dt
            listeRotation = [ref1, ref2, omega]
        else:
            listeRotation = [ref1, ref2, 0]






#--------------Initialisation---------------
fig = plt.figure()
ax = Axes3D(fig)
plt.ion()
plt.show()

axlim=50

longueur=15
largeur=10
longueurSupPatte=5
longueurInfPatte=10

longueurSup1Patte=9
longueurSup2Patte=9
longueurInf1Patte=3#pas utilisé dans cette version car fixée par les autres morceaux
longueurInf2Patte=9
angleInfPatte=0.157
centre=[0,0,5]
NW=[centre[0]-largeur*0.5,centre[1]+longueur*0.5,centre[2]]
NE=[centre[0]+largeur*0.5,centre[1]+longueur*0.5,centre[2]]
SE=[centre[0]+largeur*0.5,centre[1]-longueur*0.5,centre[2]]
SW=[centre[0]-largeur*0.5,centre[1]-longueur*0.5,centre[2]]

fixationSupNW=np.add(NW,[+0.5,0,3])
fixationSupNE=np.add(NE,[-0.5,0,3])
fixationSupSE=np.add(SE,[-0.5,0,3])
fixationSupSW=np.add(SW,[+0.5,0,3])

fixationInfNW=np.add(NW,[-0.5,0,1])
fixationInfNE=np.add(NE,[+0.5,0,1])
fixationInfSE=np.add(SE,[+0.5,0,1])
fixationInfSW=np.add(SW,[-0.5,0,1])

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

global contact0,contact1,contact2,contact3,contact, contactList
contact0=False#Permet de vérifier si chaque patte touche le sol ou non
contact1=False
contact2=False
contact3=False
contact=False #permet de vérifier si le robot est en contact avec le sol
contactList=[contact0,contact1,contact2,contact3]


dt=0.01#dt intervalle de temps en secondes
global vitesse
vitesse=[0,0,0]
g=9.81



mot0Speed=[10,10]# vitesse des moteurs pour mvt vertical et horizontal respectivement  en rad.s-1
mot1Speed=[10,10]
mot2Speed=[10,10]#[0]>0 --> patte vers le haut // [1]>0 --> patte vers l'avant
mot3Speed=[10,10]

mot0Angle=[0,0]
mot1Angle=[0,0]
mot2Angle=[0,0]
mot3Angle=[0,0]


global motSpeedList,motAngleList,motAngleLim
motAngleLim=[[3.14/5,-3.14/5],[3.14/6,-3.14/4]]#[[max,min],[max,min]]  vert,horiz
motSpeedList=[mot0Speed,mot1Speed,mot2Speed,mot3Speed]
motAngleList=[mot0Angle,mot1Angle,mot2Angle,mot3Angle]

# axesRotation : liste de listes contenant un axe et une vitesse angulaire
# [ref pied 1, ref pied 2, vitesse_angulaire]
# TODO déterminer une convention de rotation (trigo)
global listeRotation
listeRotation = []

global masseMoteur
masseMoteur = 50*10**(-3)



#------------------------------------------
