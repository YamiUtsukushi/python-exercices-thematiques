# Liste brute des clients
clients_raw = [
    ("Belhadi", "Soso", 32, "France", "epargne"),
    ("Soumare", "Hamidou", 45, "Belgique", "courant"),
    ("Mooken", "Jayson", 27, "France", "connecte"),
    ("Dupont", "Jean", 25, "France", "epargne"),
]

{
    1: {"nom": "Soso", "prenom": "Belhadi", "âge": 32, "pays": "France", "type_compte": "epargne"},
    2: {"nom": "Hamidou", "prenom": "Soumare", "âge": 45, "pays": "Belgique", "type_compte": "courant"},
    3: {"nom": "Jayson", "prenom": "Mooken", "âge": 27, "pays": "France", "type_compte": "connecte"},
    4: {"nom": "Jean", "prenom": "Dupont", "âge": 25, "pays": "France", "type_compte": "epargne"},
}

clients = {}

for i, client in enumerate(clients_raw, start=1):
    nom, prenom, age, pays, type_compte = client
    clients[i] = {
        "nom": nom,
        "prenom": prenom,
        "age": age,
        "pays": pays,
        "type_compte": type_compte
    }


import numpy as np

# Génère un tableau de soldes aléatoires
soldes = np.random.randint(50, 5000, size=len(clients))  # entre 50 et 5000 €

for i, solde in enumerate(soldes, start=1):
    clients[i]["solde"] = solde


# Liste des soldes
liste_soldes = np.array([client["solde"] for client in clients.values()])

solde_moyen = np.mean(liste_soldes)
total_depots = np.sum(liste_soldes)
nb_soldes_inf_100 = np.sum(liste_soldes < 100)

print("Solde moyen :", solde_moyen)
print("Total des dépôts :", total_depots)
print("Nombre de clients avec un solde < 100 € :", nb_soldes_inf_100)


print("\nClients avec un solde supérieur à la moyenne :")
for client in clients.values():
    if client["solde"] > solde_moyen:
        print(f"- {client['prenom']} {client['nom']} : {client['solde']} €")


def get_clients():
    return clients
