"""
🔹 Exercice 1 : Manipuler une liste de nombres
"""
def filtrer_et_trier(liste):

    filtrés = [n for n in liste if n > 10]
    filtrés.sort()
    return filtrés

résultat = filtrer_et_trier([5, 12, 8, 20, 3])
print(résultat)  

"""
🔹 Exercice 2 : Manipuler une liste de nombres
"""
def filtrer_majeurs(liste):
    prenoms = [personne[0] for personne in liste if personne[1] > 18]
    return prenoms

personnes = [("Soso", 25), ("Hamidou", 24), ("Ramdhan", 24),("Jahden", 16), ]

print(filtrer_majeurs(personnes))

"""
🔹 Exercice 3 : Compter avec un dictionnaire
"""
def compter_lettres(texte):
    compteur = {}

    for lettre in texte.lower():
        if lettre.isalpha(): 
            if lettre in compteur:
                compteur[lettre] += 1
            else:
                compteur[lettre] = 1

    return compteur

résultat = compter_lettres("Bonjour le monde")
print(résultat)

"""
🔹 Exercice 4 : Éliminer les doublons avec un set
"""

def supprimer_doublons(liste):
    unique = set(liste)
    noms_triés = sorted(unique)
    return noms_triés

noms = ["Sara", "Julie", "Sara", "Amel"]
print(supprimer_doublons(noms))



"""
🔹 Exercice 5 : Grouper les mots d'une phrase par longueur
"""

def grouper_par_longueur(phrase):
    mots = phrase.split()
    resultat = {}

    for mot in mots:
        longueur = len(mot)
        if longueur not in resultat:
            resultat[longueur] = [mot]
        else:
            resultat[longueur].append(mot)

    return resultat

print(grouper_par_longueur("Écrire une fonction qui prend une phrase et retourne un dictionnaire où chaque clé est une longueur de mot et chaque valeur est la liste des mots de cette longueur"))

