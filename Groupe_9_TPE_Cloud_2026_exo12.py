
def entier_vers_romain(n):
    # Liste des valeurs et symboles romains, des plus grands aux plus petits
    # Inclut les combinaisons spéciales (900, 400, 90, 40, 9, 4)
    valeurs = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    
    resultat = ""  # Chaîne qui contiendra le résultat final
    
    # Parcours de toutes les paires (valeur, symbole)
    for valeur, symbole in valeurs:
        # Tant que n est supérieur ou égal à la valeur courante
        while n >= valeur:
            resultat += symbole  # Ajoute le symbole romain
            n -= valeur         # Soustrait la valeur ajoutée
    
    return resultat


def romain_vers_entier(romain):
    # Dictionnaire des valeurs de base des symboles romains
    valeurs = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100,
        "D": 500, "M": 1000
    }
    
    total = 0  # Résultat final
    
    # Parcours de chaque caractère du nombre romain
    for i in range(len(romain)):
        # Cas spécial: notation soustractive
        # Si le caractère courant a une valeur inférieure au suivant
        if i + 1 < len(romain) and valeurs[romain[i]] < valeurs[romain[i + 1]]:
            # On soustrait la valeur du caractère courant
            total -= valeurs[romain[i]]
        else:
            # Sinon, on l'additionne normalement
            total += valeurs[romain[i]]
    
    return total


# ====== INTERFACE UTILISATEUR ======
print("\n====== CONVERTISSEUR ROMAIN ======")
print("1. Entier → Chiffres romains")
print("2. Chiffres romains → Entier")

choix = input("Votre choix : ")

if choix == "1":
    # Conversion entier → romain
    n = int(input("Entrez un nombre entier : "))
    print("Résultat :", entier_vers_romain(n))

elif choix == "2":
    # Conversion romain → entier
    r = input("Entrez un nombre romain : ").upper()  # Convertit en majuscules
    print("Résultat :", romain_vers_entier(r))

else:
    print("Choix invalide, réessayez.")