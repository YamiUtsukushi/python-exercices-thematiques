
# Exercice 1 – Création simple de classe
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)

# Exercice 2 – Utilisation d’attributs de classe
class Rectangle:
    nb_rectangles_crees = 0

    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        Rectangle.nb_rectangles_crees += 1

    def aire(self):
        return self.longueur * self.largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)

# Exercice 3 – Attributs d’instance vs de classe
class Tool:
    category = 'HandTool'

    def __init__(self, name):
        self.name = name

outil1 = Tool("Marteau")
outil2 = Tool("Tournevis")

print(outil1.name, "-", outil1.category)
print(outil2.name, "-", outil2.category)

# Exercice 4 – Méthodes d’instance
class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.titre = titre
        self.auteur = auteur
        self.nb_pages = nb_pages

    def resume(self):
        return f"{self.titre} écrit par {self.auteur}, contient {self.nb_pages} pages."

# Exercice 5 – Méthode de classe
class Rectangle:
    nb_rectangles_crees = 0

    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        Rectangle.nb_rectangles_crees += 1

    def aire(self):
        return self.longueur * self.largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)

    @classmethod
    def get_nbr_rectangles_crees(cls):
        return cls.nb_rectangles_crees

# Exercice 6 – Méthode statique
class Rectangle:
    @staticmethod
    def aire_rectangle(L, l):
        return L * l

# Exercice 7 – Instanciation et utilisation
r1 = Rectangle(4, 5)
r2 = Rectangle(3, 7)

print("Aire r1 :", r1.aire())
print("Périmètre r1 :", r1.perimetre())
print("Aire r2 :", r2.aire())
print("Périmètre r2 :", r2.perimetre())
print("Nombre total de rectangles :", Rectangle.get_nbr_rectangles_crees())

# Exercice 8 – Encapsulation des données
class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, val):
        if val >= 0:
            self.__longueur = val

    def set_largeur(self, val):
        if val >= 0:
            self.__largeur = val

# Exercice 9 – Utilisation de décorateurs
def log_appel(fonction):
    def wrapper(*args, **kwargs):
        print("Appel de la méthode...")
        resultat = fonction(*args, **kwargs)
        print("Méthode terminée.")
        return resultat
    return wrapper

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    @log_appel
    def aire(self):
        return self.longueur * self.largeur

# Exercice 10 – Classe avec attribut optionnel
class Livre:
    def __init__(self, titre, auteur, nb_pages=100):
        self.titre = titre
        self.auteur = auteur
        self.nb_pages = nb_pages

    def afficher(self):
        print(f"Titre : {self.titre}, Auteur : {self.auteur}, Pages : {self.nb_pages}")
