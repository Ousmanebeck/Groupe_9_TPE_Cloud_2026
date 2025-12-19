def decalage_droite(L):
    return [L[-1]] + L[:-1]  # Prend le dernier élément + tous sauf le dernier


def decalage_gauche(L):
    return L[1:] + [L[0]]  # Prend tous sauf le premier + le premier élément


# Liste initiale pour les tests
L = [0, 1, 2, 3, 4, 5]
n = len(L)  # Longueur de la liste (6 éléments)

print("Liste initiale :", L)

# ====== DÉCALAGE À DROITE ======
print("\n--- Décalage à droite ---")
temp = L.copy()  # Crée une copie pour ne pas modifier la liste originale

for i in range(n):  # On effectue n décalages (6 dans cet exemple)
    temp = decalage_droite(temp)  # Applique le décalage à droite
    print(f"Décalage {i+1} :", temp)

# ====== DÉCALAGE À GAUCHE ======
print("\n--- Décalage à gauche ---")
temp = L.copy()  # Recrée une copie fraîche de la liste originale

for i in range(n):  # On effectue n décalages (6 dans cet exemple)
    temp = decalage_gauche(temp)  # Applique le décalage à gauche
    print(f"Décalage {i+1} :", temp)