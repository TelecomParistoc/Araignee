# -*- coding: utf-8 -*-

"""modules contenant des fonctions utiles de géométrie"""

# produit scalaire : np.vdot
# produit vectoriel : np.cross

from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np


def distancePointPoint(A, B):
    return np.linalg.norm(np.subtract(B, A))


def distanceDroitePoint(point, origine, vecteur):
    """fonction qui renvoie la distance entre un point et une droite
    la droite est définie par une origine et un vecteur"""
    vecBA = np.subtract(point, origine)
    prodVec = np.cross(vecBA, vecteur)
    return np.linalg.norm(prodVec)/np.linalg.norm(vecteur)


def projeteOrtho(point, origine, vecteur):
    """fonction qui renvoie les coordonnées du projeté orthogonal d'un point sur une droite
    droite : liste de deux points"""
    d = -np.vdot(vecteur, point)
    a, b, c = 1.*vecteur[0], 1.*vecteur[1], 1.*vecteur[2]
    x, y, z = 1.*origine[0], 1.*origine[1], 1.*origine[2]
    t = -(a*x + b*y + c*z + d)/(a**2 + b**2 + c**2)
    return [a*t+x, b*t+y, c*t+z]


