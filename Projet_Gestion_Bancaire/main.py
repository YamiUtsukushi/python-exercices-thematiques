from donnees_clients import get_clients
from banque import CompteCourant, CompteEpargne, OperationInvalide, CompteConnecte, comparer_comptes

clients = get_clients()

# Compte COURANT
compte = CompteCourant(numero=101, solde=100, proprietaire="Soso Belhadi")

try:
    compte.deposer(200)     # Solde attendu : 300
    compte.retirer(700)     # Solde attendu : -400
    compte.retirer(200)     # Trop => refusé
except OperationInvalide as e:
    print("Erreur :", e)

print(compte)
compte.afficher_historique()

# Compte ÉPARGNE
epargne = CompteEpargne(numero=202, solde=1000, proprietaire="Hamidou Soumare", taux_interet=0.03)

try:
    epargne.deposer(500)         # Solde : 1500
    epargne.retirer(200)         # Solde : 1300
    epargne.retirer(2000)        # Exception levée
    epargne.appliquer_interet()  # +3%
except OperationInvalide as e:
    print("Erreur :", e)

print(epargne)
epargne.afficher_historique()


# Création d'un compte connectable
connecte = CompteConnecte(numero=303, solde=500, proprietaire="Jayson Mooken")

# Tentative de dépôt sans être connecté
try:
    connecte.deposer(100)
except OperationInvalide as e:
    print("Erreur :", e)

# Connexion
connecte.connecter()

# Dépôt après connexion
try:
    connecte.deposer(150)
    connecte.retirer(200)
except OperationInvalide as e:
    print("Erreur :", e)

# Affichage
print(connecte)
connecte.afficher_historique()


print("\n--- Comparaison entre comptes ---")
comparer_comptes(compte, epargne)        # CompteCourant vs CompteEpargne
comparer_comptes(epargne, connecte)      # CompteEpargne vs CompteConnecte
