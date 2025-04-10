# Exercices – Fondamentaux de la Programmation Orientée Objet en Python

Ce document présente une série d’exercices pour s’initier aux concepts fondamentaux des classes en Python.

## Exercice 1 – Création simple de classe

Créer une classe `Rectangle` :
- Attributs : `longueur`, `largeur`
- Méthodes :
  - `aire()` : retourne l’aire du rectangle
  - `perimetre()` : retourne le périmètre du rectangle

---

## Exercice 2 – Utilisation d’attributs de classe

Ajouter à la classe `Rectangle` :
- Un attribut de classe `nb_rectangles_crees`
- Incrémenter cet attribut à chaque création d’un nouvel objet

---

## Exercice 3 – Attributs d’instance vs de classe

Créer une classe `Tool` :
- Attribut de classe : `category = 'HandTool'`
- Attribut d’instance : `name`
- Créer plusieurs objets et afficher la différence entre attributs de classe et d’instance

---

## Exercice 4 – Méthodes d’instance

Créer une classe `Livre` :
- Attributs : `titre`, `auteur`, `nb_pages`
- Méthode : `resume()` qui retourne une phrase résumant le livre

---

## Exercice 5 – Méthode de classe

Dans la classe `Rectangle`, ajouter une méthode de classe :
- `get_nbr_rectangles_crees()` : retourne le nombre total de rectangles créés

---

## Exercice 6 – Méthode statique

Ajouter à la classe `Rectangle` :
- Une méthode statique `aire_rectangle(L, l)` : calcule l’aire sans avoir besoin d’instancier un objet

---

## Exercice 7 – Instanciation et utilisation

Créer deux objets `Rectangle` avec des dimensions différentes :
- Afficher leur aire et périmètre
- Afficher le nombre total d’instances créées

---

## Exercice 8 – Encapsulation des données

Modifier la classe `Rectangle` :
- Rendre `longueur` et `largeur` privés (`__longueur`, `__largeur`)
- Ajouter des getters et setters avec validation (refuser les valeurs négatives)

---

## Exercice 9 – Utilisation de décorateurs

Créer une fonction décoratrice `log_appel` :
- Affiche un message avant et après l’appel d’une méthode
- Appliquer ce décorateur à la méthode `aire()` de `Rectangle`

---

## Exercice 10 – Classe avec attribut optionnel

Créer une classe `Livre` :
- Paramètre `nb_pages` optionnel (valeur par défaut : 100)
- Méthode pour afficher les informations du livre