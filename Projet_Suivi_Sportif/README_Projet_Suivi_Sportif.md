# Projet Python – Système de Suivi d’Activité Sportive Connectée

Ce projet consiste à concevoir une application orientée objet permettant à des sportifs de suivre leurs activités physiques, encadrés par des coachs. Il combine POO, relations d’objets, statistiques avec NumPy et pratiques avancées de Python.

---

## 🎯 Objectifs pédagogiques

- Appliquer toutes les bases de la POO : classes, héritage, encapsulation, surcharge, décorateurs, etc.
- Utiliser des structures de données efficaces (listes, dictionnaires)
- Intégrer NumPy pour faire des analyses de performances
- Mettre en œuvre le polymorphisme et le duck typing pour créer un système flexible et générique

---

## 🧩 Composants de l’application

### Classe `Personne`
- Attributs : `nom`, `prénom`, `email` (encapsulés)
- Méthodes : `__str__`, getters/setters pour `email`

### Classe `Sportif` (hérite de `Personne`)
- Attributs : `activites` (dictionnaire : sport → liste de performances)
- Méthodes :
  - Ajouter une performance
  - Moyenne d’activité (avec NumPy)
  - `__str__` personnalisé
  - `statistique()` (pour duck typing)

### Classe `Coach` (hérite de `Personne`)
- Attributs : `spécialité`, `sportifs_suivis`
- Méthodes :
  - Ajouter un sportif
  - Calculer la progression moyenne
  - Méthode statique `valider_performance()`

### Classe `ApplicationSuivi`
- Attributs : `utilisateurs` (coachs et sportifs)
- Méthodes :
  - Ajouter une personne
  - Lister les sportifs suivis par un coach
  - Générer un rapport global (basé sur le duck typing)

---

## ✅ Contraintes et bonnes pratiques

- Les données doivent être bien structurées (listes, dictionnaires)
- Utiliser `@property`, `@staticmethod`, `@classmethod` aux bons endroits
- Utiliser des attributs protégés (`_attribut`) et privés (`__attribut`) si nécessaire
- Surcharger les méthodes (`__str__`, `__eq__`, etc.)
- Utiliser le duck typing pour traiter tout objet possédant une méthode `statistique()`

---

Ce projet permet de regrouper plusieurs concepts clés de Python avancé dans une même application concrète et réutilisable.