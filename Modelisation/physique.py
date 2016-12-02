from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np
from geometrie import*


def moment_poids(listePoints, origine, vecteur, g):
    """calcule le moment du poids autour de l'axe définit par son origine et
    un vecteur"""

    moment = [0, 0, 0]

    for elt in listePoints:
        """pour chaque élément on calcule le projete du point sur le plan
        horizontal (projete_point)on calcule le vecteur du bras de levier
        (projete_vec) et on fait le produit scalaire"""

        projete_point = [elt[0][0], elt[0][1], 0]
        projete_vec = np.subtract(projete_point, projeteOrtho(projete_point, origine, vecteur))
        p = [0, 0, -elt[1]*g]
        moment = np.add(moment, np.cross(projete_vec, p))
    return moment


def momentInertie(listePoints, origine, vector):
    # listePoints : liste de [coordonnees, masse]
    J = 0
    for point in listePoints:
        J += point[1]*(distanceDroitePoint(point[0], origine, vector))**2
    return (J)


# TODO vérifier la fonction ci-après
def axeRotation(listePoints, listePieds, centreGravite):
    """fonction qui détermine quel est l'axe de rotation du robot
    renvoie une origine et un vecteur"""

    n = len(listePoints)

    if n == 1:
        projete = centreGravite[0:2] + [0]
        vecteurNormal = np.subtract(projete, listePoints[0])
        return (listePoints[0], np.cross(vecteurNormal, [0, 0, 1]))

    elif n == 2:
        return (listePoints[0], np.subtract(listePoints[0], listePoints[1]))

    elif n == 3:
        liste = rotTriangle(listePoints, centreGravite[0:2]+[0])
        return(liste[1], liste[2])

    else:
        return (null, null)
