# Exercice 1 – Système de gestion de véhicules
from abc import ABC, abstractmethod

class Vehicule(ABC):
    def __init__(self, immatriculation):
        self._immatriculation = immatriculation

    @abstractmethod
    def afficher_infos(self):
        pass


class Voiture(Vehicule):
    def __init__(self, immatriculation, nb_portes):
        super().__init__(immatriculation)
        self.__nb_portes = nb_portes

    def afficher_infos(self):
        print("Voiture immatriculée :", self._immatriculation)
        print("Nombre de portes :", self.__nb_portes)

    @property
    def nb_portes(self):
        return self.__nb_portes

    @nb_portes.setter
    def nb_portes(self, valeur):
        if valeur > 0:
            self.__nb_portes = valeur


class Moto(Vehicule):
    def __init__(self, immatriculation, type_chaine):
        super().__init__(immatriculation)
        self.__type_chaine = type_chaine

    def afficher_infos(self):
        print("Moto immatriculée :", self._immatriculation)
        print("Type de chaîne :", self.__type_chaine)

    @property
    def type_chaine(self):
        return self.__type_chaine

    @type_chaine.setter
    def type_chaine(self, valeur):
        self.__type_chaine = valeur


v1 = Voiture("AB-123-CD", 5)
m1 = Moto("XY-987-ZW", "Renforcée")

v1.afficher_infos()
print()
m1.afficher_infos()

# Test des setters
v1.nb_portes = 3
m1.type_chaine = "Classique"
print()
v1.afficher_infos()
print()
m1.afficher_infos()

# Exercice 2 – Gestion d'un compte bancaire

from abc import ABC, abstractmethod

class Compte(ABC):
    def __init__(self, solde_initial):
        self.__solde = solde_initial

    @property
    def solde(self):
        return self.__solde

    @abstractmethod
    def deposer(self, montant):
        pass

    @abstractmethod
    def retirer(self, montant):
        pass

class CompteCourant(Compte):
    def __init__(self, solde_initial):
        super().__init__(solde_initial)

    def deposer(self, montant):
        # augmente le solde
        self._Compte__solde += montant

    def retirer(self, montant):
        if self._Compte__solde - montant >= -500:
            self._Compte__solde -= montant
        else:
            print("Découvert autorisé dépassé.")


class CompteEpargne(Compte):
    def __init__(self, solde_initial):
        super().__init__(solde_initial)

    def deposer(self, montant):
        self._Compte__solde += montant

    def retirer(self, montant):
        if self._Compte__solde - montant >= 0:
            self._Compte__solde -= montant
        else:
            print("Retrait refusé : solde insuffisant.")


cc = CompteCourant(100)
ce = CompteEpargne(200)

print("Compte courant :", cc.solde)
cc.retirer(550)  # devrait passer
cc.retirer(100)  # devrait refuser
print("Nouveau solde courant :", cc.solde)

print("\nCompte épargne :", ce.solde)
ce.retirer(250)  # devrait refuser
ce.retirer(100)  # devrait passer
print("Nouveau solde épargne :", ce.solde)

# Exercice 3 – Bibliothèque de documents

from abc import ABC, abstractmethod

class Document(ABC):
    def __init__(self, titre):
        self._titre = titre

    @abstractmethod
    def afficher_resume(self):
        pass


class Livre(Document):
    def __init__(self, titre, auteur, nb_pages):
        super().__init__(titre)
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    @property
    def auteur(self):
        return self.__auteur

    @auteur.setter
    def auteur(self, valeur):
        self.__auteur = valeur

    @property
    def nb_pages(self):
        return self.__nb_pages

    @nb_pages.setter
    def nb_pages(self, valeur):
        self.__nb_pages = valeur

    def afficher_resume(self):
        print(f"Livre : {self._titre} de {self.__auteur}, {self.__nb_pages} pages.")


class Magazine(Document):
    def __init__(self, titre, editeur, mois_publication):
        super().__init__(titre)
        self.__editeur = editeur
        self.__mois_publication = mois_publication

    @property
    def editeur(self):
        return self.__editeur

    @editeur.setter
    def editeur(self, valeur):
        self.__editeur = valeur

    @property
    def mois_publication(self):
        return self.__mois_publication

    @mois_publication.setter
    def mois_publication(self, valeur):
        self.__mois_publication = valeur

    def afficher_resume(self):
        print(f"Magazine : {self._titre}, édité par {self.__editeur}, parution : {self.__mois_publication}.")


livre1 = Livre("1984", "George Orwell", 328)
mag1 = Magazine("Science & Vie", "Uni-Éditions", "Mars 2024")

livre1.afficher_resume()
mag1.afficher_resume()


# Exercice 4 – Gestion de personnel avec surcharge
class Employe:
    def __init__(self, nom, salaire):
        self._nom = nom
        self._salaire = salaire

    def afficher_infos(self):
        print(f"Employé : {self._nom}, Salaire : {self._salaire} €")

    @property
    def salaire(self):
        return self._salaire

    @salaire.setter
    def salaire(self, valeur):
        if valeur >= 1000:
            self._salaire = valeur
        else:
            print("Erreur : le salaire ne peut pas être inférieur à 1000 €")


class Manager(Employe):
    def __init__(self, nom, salaire, bonus):
        super().__init__(nom, salaire)
        self._bonus = bonus

    def afficher_infos(self):
        super().afficher_infos()
        print(f"Bonus : {self._bonus} €")


e1 = Employe("Alice", 1500)
m1 = Manager("Bob", 2500, 800)

e1.afficher_infos()
print()
m1.afficher_infos()


# Exercice 5 – Réservation d'hébergement
from abc import ABC, abstractmethod

class Hebergement(ABC):
    def __init__(self, adresse):
        self._adresse = adresse

    @abstractmethod
    def prix_nuit(self):
        pass


class Hotel(Hebergement):
    def __init__(self, adresse, etoiles):
        super().__init__(adresse)
        self.__etoiles = etoiles

    @property
    def etoiles(self):
        return self.__etoiles

    @etoiles.setter
    def etoiles(self, valeur):
        if 1 <= valeur <= 5:
            self.__etoiles = valeur
        else:
            print("Le nombre d’étoiles doit être entre 1 et 5.")

    def prix_nuit(self):
        return 50 * self.__etoiles


class Appartement(Hebergement):
    def __init__(self, adresse, surface):
        super().__init__(adresse)
        self.__surface = surface

    @property
    def surface(self):
        return self.__surface

    @surface.setter
    def surface(self, valeur):
        if valeur > 0:
            self.__surface = valeur
        else:
            print("La surface doit être positive.")

    def prix_nuit(self):
        return 2 * self.__surface


h1 = Hotel("10 rue des potié", 4)
a1 = Appartement("25 avenue du soso", 60)

print("Prix nuit hôtel :", h1.prix_nuit(), "€")        
print("Prix nuit appartement :", a1.prix_nuit(), "€")  


# Exercice 6 – Réservation d'hébergement
from abc import ABC, abstractmethod

class Alerte(ABC):
    def __init__(self, message, date):
        self._message = message
        self._date = date

    @abstractmethod
    def envoyer_alerte(self):
        pass


class AlerteEmail(Alerte):
    def __init__(self, message, date, destinataire):
        super().__init__(message, date)
        self.__destinataire = destinataire

    @property
    def destinataire(self):
        return self.__destinataire 

    @destinataire.setter
    def destinataire(self, valeur):
        self.__destinataire = valeur

    def envoyer_alerte(self):
        print(f"[EMAIL] À : {self.__destinataire} - Message : {self._message} - Date : {self._date}")


class AlerteSMS(Alerte):
    def __init__(self, message, date, destinataire):
        super().__init__(message, date)
        self.__destinataire = destinataire

    @property
    def destinataire(self):
        return self.__destinataire

    @destinataire.setter
    def destinataire(self, valeur):
        self.__destinataire = valeur

    def envoyer_alerte(self):
        print(f"[SMS] À : {self.__destinataire} - Message : {self._message} - Date : {self._date}")


email = AlerteEmail("AlerteEmail test.", "2024-04-10", "test@example.com")
sms = AlerteSMS("AlerteSMS test : 1234", "2024-04-10", "0612345678")

email.envoyer_alerte()
sms.envoyer_alerte()
