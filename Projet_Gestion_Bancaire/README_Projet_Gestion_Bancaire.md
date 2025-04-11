# Projet Python – Système de Gestion Bancaire Avancé (POO + Exceptions)

Ce projet consiste à développer une application bancaire complète en Python, alliant gestion de données clients, statistiques avec NumPy et architecture orientée objet professionnelle.

---

## 🏦 Contexte

Une agence bancaire souhaite suivre ses clients et leurs comptes à travers :
- Une base de données clients sous forme de **dictionnaires imbriqués**
- Des **statistiques financières en temps réel** avec NumPy
- Une **modélisation orientée objet** complète et maintenable
- Une **gestion d’exceptions personnalisées** pour sécuriser les opérations

---

## 🔹 Partie 1 – Gestion de données bancaires

- Créer une liste de tuples contenant les clients : `(nom, prénom, âge, pays, type_compte)`
- Générer un dictionnaire `clients` avec un identifiant unique comme clé
- Utiliser NumPy pour :
  - Générer des **soldes aléatoires**
  - Calculer **la moyenne, le total des dépôts, et les retraits < 100 €**
- Afficher les clients avec un **solde supérieur à la moyenne**

---

## 🔸 Partie 2 – Architecture orientée objet

- **Classe abstraite `Compte`** :
  - Attributs : `__numero`, `_solde`, `proprietaire`
  - Méthodes abstraites : `deposer()`, `retirer()`
  - Méthodes spéciales : `__str__`, `__eq__`, `__len__`

- **Interface `Connectable`** :  
  - Méthode `connecter()`

- **Mixin `HistoriqueMixin`** :
  - Attribut `_historique`
  - Méthode décorée `@logger_operation` pour journaliser les actions

- **Implémentations concrètes** :
  - `CompteCourant` (découvert autorisé)
  - `CompteEpargne` (avec intérêts mensuels)
  - `CompteConnecte` (hérite de `Compte` et `Connectable`)

- **Exception personnalisée `OperationInvalide`** :
  - Déclenchée si :
    - le montant est négatif
    - le retrait dépasse les limites autorisées

- **Décorateur `@logger_operation`** :
  - Enregistre l’action effectuée
  - Ajoute un résumé dans l’historique du compte

---

## ⚙️ Script principal

- Créer les comptes à partir des données clients
- Appliquer des opérations (`deposer()`, `retirer()`, `connecter()`)
- Gérer les erreurs via `try/except`
- Afficher les historiques des comptes
- Comparer les comptes entre eux

---

## 🧠 Objectifs pédagogiques

- Modéliser un système bancaire réaliste en Python
- Utiliser l’héritage, les mixins, les décorateurs et les exceptions
- Travailler avec NumPy pour des statistiques financières
- Séparer clairement les responsabilités des classes

---

Ce projet montre comment combiner la rigueur de la POO avec la souplesse de Python pour créer un système bancaire fiable et évolutif.