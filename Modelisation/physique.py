from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np
from geometrie import*

def moment_poids(listePoints, origine, vecteur, g):
    """calcule le moment du poids autour de l'axe définit par son origine et un vecteur"""

    moment = [0, 0, 0]

    for elt in listePoints:
        """pour chaque élément on calcule le projete du point sur le plan horizontal (projete_point)
        on calcule le vecteur du bras de levier (projete_vec) et on fait le produit scalaire"""

        projete_point = [elt[0][0], elt[0][1], 0]
        projete_vec = np.subtract(projete_point, projeteOrtho(projete_point, origine, vecteur))
        p = [0,0,-elt[1]*g]
        moment = np.add(moment, np.cross(projete_vec, p))
    return moment

def momentInertie(listePoints,origine,vector):#listePoints : liste de [coordonnees,masse]
    J=0
    for point in listePoints:
        J+=point[1]*(distanceDroitePoint(point[0],origine,vector))**2
    return (J)