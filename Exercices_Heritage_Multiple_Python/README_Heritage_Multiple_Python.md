# Exercices – Python : Héritage Multiple

Ce document regroupe des exercices visant à comprendre et manipuler l'héritage multiple en Python à travers des exemples concrets.

---

## Exercice 1 : Appareil Multifonction

Créer trois classes :
- `Scanner` avec une méthode `scanner()` qui affiche "Scan en cours..."
- `Imprimante` avec une méthode `imprimer()` qui affiche "Impression en cours..."
- `Photocopieuse` qui hérite de `Scanner` et `Imprimante`, et possède une méthode `photocopier()` qui appelle les deux méthodes héritées.

Créer une instance de `Photocopieuse` et appeler les trois méthodes.

---

## Exercice 2 : Robot Cuisinier Intelligent

Créer les classes suivantes :
- `Cuisinier` avec une méthode `preparer()` qui affiche "Préparation du repas."
- `IA` avec une méthode `analyser()` qui affiche "Analyse des ingrédients."
- `RobotCuisinier` qui hérite des deux, et ajoute une méthode `executer()` qui appelle les deux méthodes précédentes.

Créer un objet `RobotCuisinier` et tester ses capacités.

---

## Exercice 3 : Gestion de rôles multiples (Mixins)

Créer une classe `Utilisateur` avec un attribut `nom`.

Créer deux mixins :
- `Loggable` avec une méthode `log()` qui affiche un message d’activité
- `Authentifiable` avec une méthode `authentifier()` qui affiche que l'utilisateur est connecté

Créer une classe `Admin` qui hérite de `Utilisateur`, `Loggable` et `Authentifiable`, et ajoute une méthode `gérer()`.

Créer un objet `Admin` et montrer qu’il peut faire toutes les actions.