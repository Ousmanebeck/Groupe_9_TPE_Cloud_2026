# Groupe_9_TPE_Cloud_2026

---

## Membres du groupe

| N° | Nom et Prénom            | Matricule  |
|----|--------------------------|------------|
| 1  | Ousmane Idriss Adam      | 23A238FS   |
| 2  | Kharachi Ahmat           |            |
| 3  | Fatimé Hamid Ambou       |            |

---

## Contributions individuelles

- **Ousmane Idriss Adam** : Encoder et décrypter un nom pour l'exercice 11

---

## Problème posé sur Exercice 11

Le problème consiste à concevoir un programme capable **d’encoder** et de **décoder** un nom tout en conservant les caractères non alphabétiques, à l’aide d’un décalage alphabétique.

---

## Explication de la résolution du problème

La solution repose sur le **chiffrement de César**, qui consiste à remplacer chaque lettre par une autre située à une position fixe plus loin dans l’alphabet.

Dans la fonction `encoder_nom`, chaque lettre du nom est d’abord transformée en **majuscule** afin d’uniformiser le traitement. Elle est ensuite convertie en **position alphabétique** (de 0 à 25) à l’aide du code ASCII. Un décalage de **3 positions** est alors appliqué. L’opération **`% 26`** permet d’assurer le retour au début de l’alphabet lorsque la fin est dépassée (après Z). La position obtenue est enfin reconvertie en lettre.

La fonction `decoder_nom` applique le processus inverse. Elle soustrait **3 positions** à chaque lettre codée afin de retrouver la lettre originale. Le modulo **26** permet d’éviter les valeurs négatives et garantit un décodage correct.

Les caractères qui ne sont pas des lettres (espaces, chiffres, symboles) sont conservés tels quels, ce qui permet de préserver la structure du nom initial.


