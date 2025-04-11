# Exercices – Python : Encapsulation, Visibilité, et Décorateurs

Ce document regroupe plusieurs exercices pour travailler les notions d'encapsulation, de visibilité des attributs, et de décorateurs en Python.

## Exercice 1 – Classe Voiture

Créer une classe `Voiture` avec :
- un attribut public `marque`
- un attribut protégé `_vitesse`
- un attribut privé `__kilometrage`
- une méthode `afficher_infos()` qui affiche les trois attributs
- un getter pour `__kilometrage`

---

## Exercice 2 – Compte Bancaire Sécurisé

Créer une classe `Compte` avec :
- un attribut privé `__solde`
- une méthode `deposer(montant)`
- une méthode `retirer(montant)` qui empêche un solde négatif
- une méthode `afficher_solde()`

---

## Exercice 3 – Utilisateur et authentification

Créer un décorateur `@authentifie` qui :
- vérifie si `user_connecte = True`
- affiche `'Accès refusé'` si False, sinon exécute la fonction

Créer une classe `Utilisateur` avec :
- un attribut privé `__mot_de_passe`
- une méthode `afficher_profil` décorée par `@authentifie`

---

## Exercice 4 – Logger personnalisé

Créer un décorateur `@logger` qui affiche :
- le nom de la fonction appelée
- les arguments reçus
- la valeur retournée

Appliquer ce décorateur sur une méthode calculatrice.

---

## Exercice 5 – Propriété avec @property et @setter

Créer une classe `Produit` avec :
- un attribut privé `__prix`
- une propriété `prix` avec `@property` pour lire sa valeur
- un setter pour contrôler que le prix est supérieur à 0

---

## Exercice 6 – Décorateur avec argument

Créer un décorateur `@repeter(n)` qui exécute une fonction `n` fois.

Appliquer ce décorateur sur une fonction `saluer()`.