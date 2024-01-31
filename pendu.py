import random

def choisir_mot():
    mots = ["python", "pendu", "programmation", "ordinateur", "developpeur", "intelligence"]
    return random.choice(mots).upper()

def afficher_mot_cache(mot, lettres_trouvees):
    mot_affiche = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_affiche += lettre
        else:
            mot_affiche += "_"
    return mot_affiche

def jouer_pendu():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = []
    tentatives_max = 6
    tentatives = 0

    print("Bienvenue dans le jeu du Pendu!")
    print(afficher_mot_cache(mot_a_deviner, lettres_trouvees))

    while tentatives < tentatives_max:
        proposition = input("Devinez une lettre : ").upper()

        if proposition in lettres_trouvees:
            print("Vous avez déjà deviné cette lettre. Essayez une autre.")
            continue

        if proposition in mot_a_deviner:
            print("Bonne devinette !")
            lettres_trouvees.append(proposition)
        else:
            print("Incorrect. Vous avez {} tentatives restantes.".format(tentatives_max - tentatives - 1))
            tentatives += 1

        mot_actuel = afficher_mot_cache(mot_a_deviner, lettres_trouvees)
        print(mot_actuel)

        if "_" not in mot_actuel:
            print("Félicitations, vous avez deviné le mot '{}'!".format(mot_a_deviner))
            break

    if "_" in mot_actuel:
        print("Dommage ! Le mot était '{}'.".format(mot_a_deviner))

if __name__ == "__main__":
    jouer_pendu()
