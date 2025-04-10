"""
🔹 Exercice 1 : Compter les voyelles
"""
def comtper_les_voylles(texte):
    voyelles = "aeiouy"
    nb_voyelles = 0
    for char in texte:
        if char in voyelles:
            nb_voyelles += 1
    print(nb_voyelles)

comtper_les_voylles("Bonjour")


"""
🔹 Exercice 2 : Pair ou impair dans une plage
"""
for i in range(10,21):
    if i % 2 == 0:
        print(i, "est pair")
    else:
        print(i, "est impair")

"""
🔹 Exercice 3 : Nombre mystère
"""
nombre = 0  # valeur de départ
mystere = 4  # le nombre à deviner

while nombre != mystere:
    nombre = int(input("Devine le nombre entre 1 et 10 : "))
    if nombre < mystere:
        print("Trop petit !")
    elif nombre > mystere:
        print("Trop grand !")

print("Bravo, tu as trouvé le nombre mystère !")

"""
🔹 Exercice 4 : Compteur de majuscules
"""

def compter_majuscules(maj):
    compteur = 0
    for lettre in maj:
        if lettre.isupper():
            compteur += 1
    return compteur

print(compter_majuscules("Bonjour Tous LE MONDE"))

"""
🔹 Exercice 5 :  Générateur de carré d'étoiles
"""
n = int(input("Entrez un nombre : "))
for i in range(n):
    for j in range(n):
        print("⭐", end="")
    print()

"""
🔹 Exercice 6 : Vérificateur d'âge
"""
def verif_age(age):
    if age >= 18:
        return True
    else:
        return False

mon_age = int(input("Entrez un âge : "))
print(verif_age(mon_age))

"""
🔹 Exercice 7 : Carnet de notes automatisé
"""

nb_etudiant = int(input("Entrez le nombre d'élèves : "))
eleves = {}

for i in range(nb_etudiant):
    nom = input("Entrez le nom de l'élève : ")
    note = float(input("Entrez la note de l'élève : "))
    eleves[nom] = note

somme = 0
for note in eleves.values():
    somme += note

moyenne = somme / nb_etudiant
print("Moyenne générale :", moyenne)

for eleve_nom, eleve_note in eleves.items():
    if eleve_note > 10:
        print(f"{eleve_nom} a eu {eleve_note}/20")

"""
🔹 Exercice 8 : Gestionnaire de mots de passe
"""
while True:
    mot_de_passe = input("Entrez un mot de passe : ")

    # Vérifie les conditions
    long_ok = len(mot_de_passe) >= 8
    maj_ok = any(c.isupper() for c in mot_de_passe)
    chiffre_ok = any(c.isdigit() for c in mot_de_passe)

    if long_ok and maj_ok and chiffre_ok:
        print("Mot de passe valide !")
        break
    else:
        print("Mot de passe invalide. Il doit faire au moins 8 caractères, contenir une majuscule et un chiffre.")
