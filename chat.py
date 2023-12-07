grid: list[int] = [0, 0, 2, 2]

def afficher_grille(grille):
    i = 0
    while i < 4:
        print(grille[i])
        i += 1

def deplacer_a_gauche(grille):
    direction: str = input("Q").upper()
    n: int = 0
    k: int = 1
    if direction == "Q":
        while n < len(grille):
            while n + k < len(grille) and grille[n + k] == 0:
                k += 1

            if n + k < len(grille):
                grille[n] = grille[n + k]
                grille[n + k] = 0

            k = 1  # Réinitialiser k pour la prochaine itération
            n += 1

# Grille initiale
print(grid)

# Déplacer les éléments à gauche
deplacer_a_gauche(grid)

# Afficher la grille après le déplacement à gauche
print(grid)