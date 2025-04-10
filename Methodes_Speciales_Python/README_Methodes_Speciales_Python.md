# Exercice – Méthodes Spéciales en Python

Cet exercice a pour but de mettre en pratique les méthodes spéciales en Python (`__len__`, `__getitem__`, `__contains__`, `__str__`) à travers la création d'une classe personnalisée.

---

## Objectif

Créer une classe `CarnetContacts` qui représente un carnet d’adresses. Ce carnet devra :

- Stocker une **liste de contacts**, où chaque contact est une chaîne de caractères représentant un nom.

---

## Méthodes Spéciales à implémenter

- `__len__` : Retourne le nombre total de contacts dans le carnet.
- `__getitem__` : Permet d’accéder à un contact via son index.
- `__contains__` : Permet de vérifier si un nom donné est présent dans le carnet.
- `__str__` : Retourne une représentation lisible du carnet avec tous les noms.

---

## Exemple d’utilisation attendue

```python
carnet = CarnetContacts()

carnet.ajouter("Alice")
carnet.ajouter("Bob")

print(len(carnet))         # 2
print("Alice" in carnet)   # True
print(carnet[0])           # Alice
print(carnet)              # Carnet: Alice, Bob
```