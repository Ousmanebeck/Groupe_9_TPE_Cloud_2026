#Fonction pour encoder
def encoder_nom(nom):
    nom_encode = ""
    for lettre in nom.upper():
        if lettre.isalpha():
            # Conversion de la lettre en code ASCII, ajout du décalage, et retour dans l'alphabet
            code = ord(lettre) - ord('A')  # A devient 0, B devient 1, etc.
            code_encode = (code + 3) % 26  # Décalage de 3 avec bouclage
            lettre_encodee = chr(code_encode + ord('A'))
            nom_encode += lettre_encodee
        else:
            # Si ce n'est pas une lettre, on laisse tel quel
            nom_encode += lettre
    return nom_encode

def decoder_nom(nom_encode):
    nom_decode = ""
    for lettre in nom_encode.upper():
        if lettre.isalpha():
            # Conversion de la lettre en code ASCII, soustraction du décalage, et retour dans l'alphabet
            code = ord(lettre) - ord('A')
            code_decode = (code - 3) % 26  # Décalage inverse de 3 avec bouclage
            lettre_decodee = chr(code_decode + ord('A'))
            nom_decode += lettre_decodee
        else:
            # Si ce n'est pas une lettre, on laisse tel quel
            nom_decode += lettre
    return nom_decode

print("=== Programme d'encodage/décodage pour agents secrets ===")

# Partie 1 : Encodage
print("\n--- Phase d'encodage ---")
nom_agent = input("Entrez le nom de l'agent secret : ")
nom_encode = encoder_nom(nom_agent)
print(f"Nom encodé : {nom_encode}")

# Partie 2 : Décodage
print("\n--- Phase de décodage ---")
nom_code = input("Entrez un nom encodé à décrypter : ")
nom_decode = decoder_nom(nom_code)
print(f"Nom décodé : {nom_decode}")