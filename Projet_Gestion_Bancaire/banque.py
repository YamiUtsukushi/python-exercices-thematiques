from abc import ABC, abstractmethod

class Compte(ABC):
    def __init__(self, numero, solde, proprietaire):
        self.__numero = numero
        self._solde = solde
        self.proprietaire = proprietaire

    @abstractmethod
    def deposer(self, montant):
        pass

    @abstractmethod
    def retirer(self, montant):
        pass

    # Affiche proprement un compte
    def __str__(self):
        return f"Compte #{self.__numero} - Propriétaire : {self.proprietaire} - Solde : {self._solde} €"

    # Compare deux comptes par solde
    def __eq__(self, other):
        return self._solde == other._solde

    # Retourne la longueur comme... le nombre de chiffres du solde ? (ou du numéro, selon ton choix)
    def __len__(self):
        return len(str(self._solde))


class Connectable:
    def connecter(self):
        print(f"{self.__class__.__name__} connecté avec succès.")


class HistoriqueMixin:
    def __init__(self):
        self._historique = []

    def afficher_historique(self):
        print("\nHistorique :")
        for ligne in self._historique:
            print("-", ligne)


def logger_operation(fonction):
    def wrapper(self, *args, **kwargs):
        resultat = fonction(self, *args, **kwargs)
        operation = f"{fonction.__name__} appelé avec {args}"
        self._historique.append(operation)
        return resultat
    return wrapper

class CompteCourant(Compte, HistoriqueMixin):
    def __init__(self, numero, solde, proprietaire):
        Compte.__init__(self, numero, solde, proprietaire)
        HistoriqueMixin.__init__(self)

    @logger_operation
    def deposer(self, montant):
        if montant <= 0:
            raise OperationInvalide("Le montant déposé doit être positif.")
        self._solde += montant
       
    @logger_operation
    def retirer(self, montant):
        if montant <= 0:
            raise OperationInvalide("Le montant retiré doit être positif.")
        if self._solde - montant < -500:
            raise OperationInvalide("Le découvert autorisé est dépassé.")
        self._solde -= montant


class CompteEpargne(Compte, HistoriqueMixin):
    def __init__(self, numero, solde, proprietaire, taux_interet):
        Compte.__init__(self, numero, solde, proprietaire)
        HistoriqueMixin.__init__(self)
        self.__taux_interet = taux_interet 

    @logger_operation
    def deposer(self, montant):
        if montant <= 0:
            raise OperationInvalide("Le montant déposé doit être supérieur à 0.")
        self._solde += montant

    @logger_operation
    def retirer(self, montant):
        if montant <= 0:
            raise OperationInvalide("Le montant retiré doit être supérieur à 0.")
        if self._solde - montant < 0:
            raise OperationInvalide("Solde insuffisant pour effectuer ce retrait.")
        self._solde -= montant

    @logger_operation
    def appliquer_interet(self):
        interet = self._solde * self.__taux_interet
        self._solde += interet
        self._historique.append(f"Intérêt de {interet:.2f} € appliqué.")
        return interet

class OperationInvalide(Exception):
    def __init__(self, message):
        super().__init__(message)



class CompteConnecte(Compte, Connectable, HistoriqueMixin):
    def __init__(self, numero, solde, proprietaire):
        Compte.__init__(self, numero, solde, proprietaire)
        HistoriqueMixin.__init__(self)
        self.__en_ligne = False

    def connecter(self):
        self.__en_ligne = True
        print(f"\n Compte connecté avec succès.")

    @logger_operation
    def deposer(self, montant):
        if not self.__en_ligne:
            raise OperationInvalide("Le compte n'est pas connecté.")
        if montant <= 0:
            raise OperationInvalide("Le montant déposé doit être positif.")
        self._solde += montant

    @logger_operation
    def retirer(self, montant):
        if not self.__en_ligne:
            raise OperationInvalide("Le compte n'est pas connecté.")
        if montant <= 0:
            raise OperationInvalide("Le montant retiré doit être positif.")
        if self._solde - montant < 0:
            raise OperationInvalide("Solde insuffisant.")
        self._solde -= montant

def comparer_comptes(c1, c2):
    if c1 == c2:
        print("Les deux comptes ont le même solde.")
    elif c1._solde > c2._solde:
        print(f"{c1.proprietaire} a un solde plus élevé.")
    else:
        print(f"{c2.proprietaire} a un solde plus élevé.")
