# Exercice 1 –  Appareil Multifonction
class Scanner:
    def scanner(self):
        print("Scan en cours...")

class Imprimante:
    def imprimer(self):
        print("Impression en cours...")

class Photocopieuse(Scanner, Imprimante):
    def photocopier(self):
        self.scanner()
        self.imprimer()


appareil = Photocopieuse()

appareil.scanner()       # Scan en cours...
appareil.imprimer()      # Impression en cours...
appareil.photocopier()   # Scan en cours... + Impression en cours...

# Exercice 2 –  Robot Cuisinier Intelligent
class Cuisinier:
    def preparer(self):
        print("Préparation du repas.")

class IA:
    def analyser(self):
        print("Analyse des ingrédients.")

class RobotCuisinier(Cuisinier, IA):
    def executer(self):
        self.preparer()
        self.analyser()

robot = RobotCuisinier()

robot.preparer()    # Préparation du repas...
robot.analyser()    # Analyse des ingrédients.
robot.executer()    # Préparation du repas... + Analyse des ingrédients.

# Exercice 3 –  Gestion de rôles multiples (Mixins)
class Utilisateur:
    def __init__(self, nom):
        self.nom = nom

class Loggable:
    def log(self):
        print(f"Utilisateur {self.nom} a effectué une action.")

class Authentifiable:
    def authentifier(self):
        print(f"Utilisateur {self.nom} est connecté.")

class Admin(Utilisateur, Loggable, Authentifiable):
    def gérer(self):
        print(f"{self.nom} gère le système.")

admin1 = Admin("Soso")

admin1.authentifier()   # → Utilisateur Sophie est connecté.
admin1.log()            # → Utilisateur Sophie a effectué une action.
admin1.gérer()          # → Soso gère le système.
