class Personne:
    def __init__(self, nom, prenom, email):
        self.__nom = nom
        self.__prenom = prenom
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valeur):
        self.__email = valeur

    def __str__(self):
        return f"{self.__prenom} {self.__nom} - Email : {self.__email}"


# Création d'une instance
p1 = Personne("Dupont", "Julie", "julie.dupont@email.com")

# Affichage avec __str__
print(p1)

# Lecture de l'e-mail
print("Email :", p1.email)

# Modification de l'e-mail
p1.email = "nouvel.email@email.com"
print("Email mis à jour :", p1.email)

import numpy as np

class Sportif(Personne):
    def __init__(self, nom, prenom, email):
        super().__init__(nom, prenom, email)
        self._activites = {}

    def ajouter_performance(self, sport, valeur):
        if sport not in self._activites:
            self._activites[sport] = []
        self._activites[sport].append(valeur)

    def moyenne_activite(self, sport):
        if sport in self._activites and self._activites[sport]:
            return np.mean(self._activites[sport])
        else:
            return None

    def statistique(self):
        return {sport: self.moyenne_activite(sport) for sport in self._activites}

    def __str__(self):
        return f"[Sportif] {super().__str__()} | Activités : {list(self._activites.keys())}"

s1 = Sportif("Durand", "Lucas", "lucas.durand@email.com")

s1.ajouter_performance("course", 12)
s1.ajouter_performance("course", 10)
s1.ajouter_performance("natation", 30)

print(s1)  # Affiche les infos de base + les sports suivis

print("Moyenne course :", s1.moyenne_activite("course"))
print("Statistiques :", s1.statistique())


class Coach(Personne):
    def __init__(self, nom, prenom, email, specialite):
        super().__init__(nom, prenom, email)
        self._specialite = specialite
        self._sportifs = []

    def ajouter_sportif(self, sportif):
        self._sportifs.append(sportif)

    def progression_moyenne(self):
        moyennes = []
        for sportif in self._sportifs:
            stats = sportif.statistique()
            valeurs = [val for val in stats.values() if val is not None]
            if valeurs:
                moyennes.append(np.mean(valeurs))
        return np.mean(moyennes) if moyennes else 0

    @staticmethod
    def valider_performance(valeur):
        return valeur > 0

    def __str__(self):
        return f"[Coach] {super().__str__()} | Spécialité : {self._specialite} | Sportifs suivis : {len(self._sportifs)}"


# Création de deux sportifs
s1 = Sportif("Durand", "Lucas", "lucas@email.com")
s2 = Sportif("Martin", "Emma", "emma@email.com")

# Ajout de performances
s1.ajouter_performance("course", 12)
s1.ajouter_performance("course", 10)
s2.ajouter_performance("natation", 30)
s2.ajouter_performance("natation", 40)

# Création d'un coach
coach = Coach("Legrand", "Thomas", "thomas@email.com", "Endurance")

# Ajout des sportifs au coach
coach.ajouter_sportif(s1)
coach.ajouter_sportif(s2)

# Affichage
print(coach)  # Info coach
print("Progression moyenne des sportifs :", coach.progression_moyenne())  # Moyenne globale
print("Performance valide (25) ?", Coach.valider_performance(25))        # True
print("Performance valide (-2) ?", Coach.valider_performance(-2))        # False


class ApplicationSuivi:
    def __init__(self):
        self.utilisateurs = []

    def ajouter_personne(self, personne):
        self.utilisateurs.append(personne)

    def lister_sportifs_coach(self, coach):
        if isinstance(coach, Coach):
            return coach._sportifs
        else:
            return []

    def rapport_global(self):
        print("=== Rapport Global ===")
        for utilisateur in self.utilisateurs:
            if hasattr(utilisateur, "statistique") and callable(utilisateur.statistique):
                print(f"{utilisateur}")
                print("Stats :", utilisateur.statistique())


# Création des sportifs
s1 = Sportif("Durand", "Lucas", "lucas@email.com")
s2 = Sportif("Martin", "Emma", "emma@email.com")
s1.ajouter_performance("course", 10)
s1.ajouter_performance("course", 12)
s2.ajouter_performance("natation", 25)
s2.ajouter_performance("natation", 30)

# Création du coach
coach = Coach("Legrand", "Thomas", "thomas@email.com", "Endurance")
coach.ajouter_sportif(s1)
coach.ajouter_sportif(s2)

# Création de l'application
app = ApplicationSuivi()

# Ajout des utilisateurs à l'application
app.ajouter_personne(s1)
app.ajouter_personne(s2)
app.ajouter_personne(coach)

# Liste des sportifs du coach
print("\nListe des sportifs du coach :")
for sportif in app.lister_sportifs_coach(coach):
    print("-", sportif)

# Rapport global
print("\n Rapport global :")
app.rapport_global()
