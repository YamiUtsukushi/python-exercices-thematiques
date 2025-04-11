# Exercices Avancés – Héritage, Surcharge et Classes Abstraites en Python

Ce document propose une série d’exercices pour maîtriser l’héritage, la surcharge de méthodes et l’utilisation des classes abstraites en Python.

## Exercice 1 – Système de gestion de véhicules

Créer une classe abstraite `Vehicule` avec :
- une méthode abstraite `afficher_infos()`
- un attribut protégé `_immatriculation`
- un constructeur pour initialiser l’immatriculation

Créer deux classes :
- `Voiture` : hérite de `Vehicule`, ajoute `__nb_portes` avec getter/setter
- `Moto` : hérite de `Vehicule`, ajoute `__type_chaine` avec getter/setter

Chaque classe redéfinit `afficher_infos()`. Tester avec plusieurs objets.

---

## Exercice 2 – Gestion d’un compte bancaire

Créer une classe abstraite `Compte` avec :
- un attribut privé `__solde`
- des méthodes abstraites `deposer()` et `retirer()`
- un getter `@property` pour le solde

Créer deux sous-classes :
- `CompteCourant` : autorise un découvert jusqu’à -500€
- `CompteEpargne` : interdit tout découvert

Utiliser `super()` pour initialiser le solde.

---

## Exercice 3 – Bibliothèque de documents

Créer une classe abstraite `Document` avec :
- un attribut `_titre`
- une méthode abstraite `afficher_resume()`

Créer deux sous-classes :
- `Livre` : attributs `__auteur`, `__nb_pages` (avec propriétés)
- `Magazine` : attributs `__editeur`, `__mois_publication` (avec propriétés)

Chaque sous-classe redéfinit `afficher_resume()`.

---

## Exercice 4 – Gestion de personnel avec surcharge

Créer une classe `Employe` avec :
- attributs protégés `_nom`, `_salaire`
- méthode `afficher_infos()`
- propriété `salaire` avec un setter refusant un salaire < 1000€

Créer une sous-classe :
- `Manager` : surcharge `afficher_infos()` pour inclure un bonus, utilise `super()`

---

## Exercice 5 – Réservation d’hébergement

Créer une classe abstraite `Hebergement` avec :
- un constructeur pour l’adresse
- une méthode abstraite `prix_nuit()`

Créer deux sous-classes :
- `Hotel` : attribut `__etoiles` (avec décorateurs)
- `Appartement` : attribut `__surface` (avec décorateurs)

Le prix par nuit dépend du type d’hébergement et de ses attributs.

---

## Exercice 6 – Système d’alertes

Créer une classe abstraite `Alerte` avec :
- une méthode `envoyer_alerte()`

Créer deux sous-classes :
- `AlerteEmail`
- `AlerteSMS`

Chaque classe redéfinit la méthode. Ajouter des attributs privés pour les destinataires avec getters/setters. Utiliser `super()` pour initialiser les attributs partagés.