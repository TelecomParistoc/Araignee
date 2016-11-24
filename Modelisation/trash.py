"""fichier qui contient du code inachevé et des fonctions abandonnées"""


def momentCinetique(droite):
    """fonction qui renvoie le moment cinétique du robot """


def reactionsNormales(centreGravite, couplesVert):
    """fonction qui renvoie les vecteurs correspondant aux réactions normales du support
    pour chaque pied de l'araignée
    couplesVert : liste des couples des moteurs dont la rotation est verticale"""

    listeReactions = [0, 0, 0, 0]

    # on établit la liste des points en contact avec le sol
    listePointContact = []
    listeRefContact = [] # liste des numéros des pattes impliquées
    if contact0:
        listePointContact.append(ObjetParNom["patte0Inf2"][0])
        listeRefContact.append(0)
    if contact1:
        listePointContact.append(ObjetParNom["patte1Inf2"][0])
        listeRefContact.append(1)
    if contact2:
        listePointContact.append(ObjetParNom["patte2Inf2"][0])
        listeRefContact.append(2)
    if contact3:
        listePointContact.append(ObjetParNom["patte3Inf2"][0])
        listeRefContact.append(3)

    # s'il y a deux points de contact
    if len(listePointContact) == 2:
        projG = projeteOrtho(centreGravite, [listePointContact[0],listePointContact[1]])
        #TODO fonction qui renvoie le moment cinétique autour d'un axe donné
        # pour l'instant on part du principe qu'il est nul (a priori il l'est)
        i, j = listeRefContact[0], listeRefContact[1]
        Li, Lj = distancePointPoint(projG, listePointContact[0]), distancePointPoint(projG, listePointContact[1])
        listeReactions[i], listeReactions[j] = poids*(Lj/(Lj+Li)), poids*(Li/(Lj+Li))
        #TODO ajouter l'impact des couples moteurs

    #TODO cas à trois points de contacts et à quatres

    return listeReactions
