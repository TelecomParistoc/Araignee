from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np
from geometrie import*

def moment_poids(listePoints, origine, vecteur, g):
    moment = [0, 0, 0]
    a, b, c = 1.*vecteur[0], 1.*vecteur[1], 1.*vecteur[2]
    x, y, z = 1.*origine[0], 1.*origine[1], 1.*origine[2]
    for elt in listePoints:
        projete_point = [elt[0][0], elt[0][1], 0]
        projete_vec = np.subtract(projete_point, projeteOrtho(projete_point, origine, vecteur))
        p = [0,0,-elt[1]*g]
        moment = np.add(moment, np.cross(projete_vec, p))
    return moment