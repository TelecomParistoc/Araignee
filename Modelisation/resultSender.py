# -*- coding: utf-8 -*-

from testRobotSimple import*
import sys

max = 50
nbit = 8
maxbit = 2**(nbit-1)
coeff = max/maxbit

sequence = sys.argv[1]

sequence = sequence.split(";")

for elt in sequence:
    n = int(len(elt)/8)
    elt = [elt[j*8:(j+1)*8] for j in range(n)]
    for elt2 in elt:
        elt2 = coeff * (int(elt2, 2) - 2 * maxbit)


with open("data", "w") as fichier:
    fichier.write("")


with open("data", "a") as fichier:
    for j, elt in sequence:
        droite = [elt[2*i] for i in range(len(elt)/2)]
        gauche = [elt[(2*i)+1] for i in range(len(elt)/2)]
        liste = [doite, gauche]
        fichier.write(str(stepByStep(liste))+'\n')
