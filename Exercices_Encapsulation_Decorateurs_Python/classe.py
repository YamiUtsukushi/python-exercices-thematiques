# Exercice 1 – Classe Voiture
class Voiture:
    def __init__(self, marque, vitesse, kilometrage):
        self.marque = marque             # public
        self._vitesse = vitesse          # protégé
        self.__kilometrage = kilometrage # privé

    def afficher_infos(self):
        print("Marque :", self.marque)
        print("Vitesse :", self._vitesse)
        print("Kilométrage :", self.__kilometrage)

    @property
    def kilometrage(self):
        return self.__kilometrage
    
voiture = Voiture("Renault", 120, 45000)

voiture.afficher_infos()
print("Accès via getter :", voiture.kilometrage)

# Exercice 2 – Compte Bancaire Sécurisé
class Compte:
    def __init__(self, solde_initial):
        self.__solde = solde_initial  # privé

    def deposer(self, montant):
        self.__solde += montant

    def retirer(self, montant):
        if self.__solde >= montant:
            self.__solde -= montant
        else:
            print("Fonds insuffisants.")

    def afficher_solde(self):
        print("Solde actuel :", self.__solde)
    
    @property
    def solde(self):
        return self.__solde
    
    @solde.setter
    def solde(self, valeur):
        if valeur >= 0:
            self.__solde = valeur
        else:
            print("Erreur : le solde ne peut pas être négatif.")


compte = Compte(100)
print("Accès direct via @property :", compte.solde)  # → 100
compte.afficher_solde()  # Solde actuel : 100
compte.deposer(50)
compte.afficher_solde()  # Solde actuel : 150
compte.retirer(70)
compte.afficher_solde()  # Solde actuel : 80
compte.retirer(100)      # Fonds insuffisants.


print(compte.solde)  # 100

compte.solde = 300
print(compte.solde)  # 300

compte.solde = -50   # Affiche : Erreur : le solde ne peut pas être négatif.
print(compte.solde)  # Toujours 300

# Exercice 3 – Utilisateur et authentification
def authentifie(fonction):
    def wrapper(self, *args, **kwargs):
        if self.user_connecte == True:
            return fonction(self, *args, **kwargs)
        else:
            print("Accès refusé")
    return wrapper

class Utilisateur:
    def __init__(self, mot_de_passe):
        self.__mot_de_passe = mot_de_passe
        self.user_connecte = False  # déconnecté par défaut

    @authentifie
    def afficher_profil(self):
        print("Bienvenue dans votre profil !")

    def connecter(self, mdp):
        if mdp == self.__mot_de_passe:
            self.user_connecte = True
            print("Connexion réussie.")
        else:
            print("Mot de passe incorrect.")

u = Utilisateur("1234")
u.afficher_profil()          # Accès refusé
u.connecter("azerty")        # Mot de passe incorrect
u.connecter("1234")          # Connexion réussie
u.afficher_profil()          # Bienvenue dans votre profil !

# Exercice 4 – Logger personnalisé

def logger(fonction):
    def wrapper(*args, **kwargs):
        print("Fonction appelée :", fonction.__name__)
        print("Arguments :", args, kwargs)
        resultat = fonction(*args, **kwargs)
        print("Valeur retournée :", resultat)
        return resultat
    return wrapper

class Calculatrice:
    @logger
    def addition(self, a, b):
        return a + b

calc = Calculatrice()
resultat = calc.addition(5, 3)

# Exercice 5 – Propriété avec @property et @setter
class Produit:
    def __init__(self, prix):
        self.__prix = prix

    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, valeur):
        if valeur > 0:
            self.__prix = valeur
        else:
            print("Le prix doit être supérieur à 0.")

p = Produit(50)
print(p.prix)       # 50

p.prix = 100
print(p.prix)       # 100

p.prix = -20        # Le prix doit être supérieur à 0.
print(p.prix)       # 100 (ça n'a pas changé)


# Exercice 6 – Décorateur avec argument

def repeter(n):
    def decorateur(fonction):
        def wrapper(*args, **kwargs):
            for i in range(n):
                fonction(*args, **kwargs)
        return wrapper
    return decorateur

@repeter(3)
def saluer():
    print("Bonjour !")

saluer()

