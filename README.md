# Groupe_9_TPE_Cloud_2026

## Présentation du projet
Ce dépôt contient les travaux réalisés par le **Groupe 9** dans le cadre du **TPE de Cloud Computing 2026**.  
Les exercices portent sur des algorithmes fondamentaux, leur implémentation et leur explication détaillée.

---

## Membres du groupe

| N° | Nom et Prénom              | Matricule |
|----|----------------------------|-----------|
| 1  | AHMAT ALI AL-IKHEDIR       | 23A322FS  |
| 2  | FATIME HAMID AMBOU         | 23B080FS  |
| 3  | KHARACHI AHMAT ADOUM       | 23B144FS  |
| 4  | MOHAMED ARAFAT             | 23A565FS  |
| 5  | FATCHOU DANZLADA           | 22A981FS  |
| 6  | OUSMANE IDRISS ADAM        | 23A238FS  |

---

##Contributions individuelles par exercice

###Exercice 11 : Encodage et décodage de noms (Chiffrement de César)
- **Ousmane Idriss Adam**  
  Implémentation de l’algorithme de chiffrement.
- **FATCHOU DANZLADA**  
 Implémentation de l’algorithme de déchiffrement.

---

###Exercice 12 : Convertisseur de chiffres romains
- **KHARACHI AHMAT ADOUM**
  Algorithme de conversion *entier → chiffres romains*.
  
- **AHMAT ALI AL-IKHEDIR**  
  Algorithme de conversion *chiffres romains → entier*

---

### Exercice 13 : Décalage circulaire d’une liste
- **Fatime Hamid Ambou**  
 Développement des fonctions `decalage_droite`.
- **Mohamed Arafat**  
   Développement des fonctions `decalage_gauche`.

---

##Exercice 11 : Chiffrement de César

###Problème posé
Concevoir un programme capable **d’encoder** et de **décoder** un nom à l’aide d’un décalage alphabétique, tout en conservant les caractères non alphabétiques (espaces, chiffres, symboles).

###Explication de la résolution
La solution repose sur le **chiffrement de César**, qui consiste à remplacer chaque lettre par une autre située à une position fixe plus loin dans l’alphabet.

- Chaque lettre est convertie en **majuscule** pour uniformiser le traitement.
- Elle est transformée en position alphabétique (0 à 25) à l’aide du code ASCII.
- Un **décalage de 3 positions** est appliqué.
- L’opération **modulo 26 (`% 26`)** permet de revenir au début de l’alphabet après Z.
- La position obtenue est reconvertie en lettre.

La fonction `decoder_nom` applique le processus inverse en soustrayant 3 positions.  
Les caractères non alphabétiques sont conservés tels quels afin de préserver la structure du nom original.

---

## Exercice 12 : Convertisseur de chiffres romains

### Problème posé
Créer un programme capable de :
- Convertir un nombre entier en chiffres romains
- Convertir des chiffres romains en nombre entier
- Gérer la notation **additive** et **soustractive**

### Principe des chiffres romains
Le système romain repose sur sept symboles :

| Symbole | Valeur |
|--------|--------|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

Deux types de notation sont utilisés :
- **Additive** : les valeurs s’additionnent (ex : `III = 3`, `VI = 6`)
- **Soustractive** : une valeur plus petite placée avant une plus grande se soustrait  
  (ex : `IV = 4`, `IX = 9`)

---

##Exercice 13 : Décalage circulaire d’une liste

###Problème posé
Implémenter un **décalage circulaire** des éléments d’une liste, où chaque élément prend la place de son voisin et l’élément en bordure revient à l’extrémité opposée.

###Explication de la résolution

####Décalage à droite (`decalage_droite`)
**Principe** :  
Le dernier élément devient le premier, tous les autres sont décalés d’une position vers la droite.

**Mécanisme** :
- `L[-1]` : récupère le dernier élément
- `L[:-1]` : récupère tous les éléments sauf le dernier
- `[L[-1]] + L[:-1]` : forme la nouvelle liste

####Décalage à gauche (`decalage_gauche`)
**Principe** :  
Le premier élément devient le dernier, tous les autres sont décalés vers la gauche.

**Mécanisme** :
- `L[1:]` : récupère tous les éléments sauf le premier
- `[L[0]]` : récupère le premier élément
- `L[1:] + [L[0]]` : forme la nouvelle liste

---
