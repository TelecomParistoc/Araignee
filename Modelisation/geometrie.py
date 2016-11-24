# -*- coding: utf-8 -*-

"""modules contenant des fonctions utiles de géométrie"""

from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np


def distancePointPoint(A, B):
    return np.linalg.norm([B[i]-A[i] for i in range(3)])


def distanceDroitePoint(point, origine, vecteur):
    """fonction qui renvoie la distance entre un point et une droite en fonction des coordonnées
    du point et des points définissant la droite
    droite : liste de deux points"""
    droite = [origine, np.add(origine, vecteur)]
    vecBA = [point[i]-droite[0][i] for i in range(3)]
    vecDir = [droite[1][i]-droite[0][i] for i in range(3)]
    prodVec = [vecBA[(i+1)%3]*vecDir[(i+2)%3]-vecBA[(i+2)%3]*vecDir[(i+1)%3] for i in range(3)]
    return np.linalg.norm(prodVec)/np.linalg.norm(vecDir)


def projeteOrtho(point, origine, vecteur):
    """fonction qui renvoie les coordonnées du projeté orthogonal d'un point sur une droite
    droite : liste de deux points"""
    d = -sum([vecteur[i]*point[i] for i in range(3)])
    a, b, c = vecteur[0], vecteur[1], vecteur[2]
    x, y, z = origine[0], origine[1], origine[2]
    t = -(a*x + b*y + c*z + d)/(a**2 + b**2 + c**2)
    return [a*t+x, b*t+y, c*t+z]

