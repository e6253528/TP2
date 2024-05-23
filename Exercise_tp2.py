"""
#Exercise 1

import csv
import json

def lire_fichier_nbcomplexe(fichier_json):

    with open(fichier_json, 'r') as f:
        data = json.load(f)

    return data

def ecrire_nbcomplexe(data, fichier_csv):
    with open(fichier_csv, 'w', newline='') as f_2:

        ecrire_csv = csv.writer(f_2)
        ecrire_csv.writerow(['reel', 'imaginaire'])

        for complex_number in data:
            ecrire_csv.writerow(complex_number)

# Exemple d'utilisation
json_filename = 'data.json'
csv_filename = 'complex_numbers.csv'

# Lire les nombres complexes du fichier JSON
nb_complexe = lire_fichier_nbcomplexe(json_filename)
# Écrire les nombres complexes dans le fichier CSV
ecrire_nbcomplexe(nb_complexe, csv_filename)

print("Les nombres complexes ont été écrits dans le fichier CSV avec succès.")

"""

"""
#Exercise 2

import csv

def lire_donnees(filename):

    donnees_pokemon = {}

    with open(filename, mode='r', newline='') as f:
        lire_csv = csv.reader(f)

        # Parcourir le fichier csv par chaque ligne

        for ligne in lire_csv:
            nom = ligne[0]  # Puisque le nom du pokemon se trouve à la position [0], je l'extrait.
            donnees = list(map(int, ligne[1:])) # Utilisation de la fonction map pour transformer toutes les données en int
            donnees_pokemon[nom] = donnees  # Stocker le nom et les donnees dans le dictionnaire

    return donnees_pokemon

def afficher_donnees(donnees_pokemon):

    for nom, donnees in donnees_pokemon.items():
        print(f"{nom}: {donnees}")

def charger_pokemons_csv(filename):
    return lire_donnees(filename)


filename = 'pokemon.csv'
donnees_pokemon = charger_pokemons_csv(filename)
afficher_donnees(donnees_pokemon)


print(isinstance(donnees_pokemon, dict))
print(isinstance(donnees_pokemon["Pikachu"], list))
print(isinstance(donnees_pokemon["Pikachu"][0], int))
"""

