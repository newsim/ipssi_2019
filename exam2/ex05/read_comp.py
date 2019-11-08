#!/usr/bin/python3

fichier = open("../docker-compose.yml", "r")
    
for ligne in fichier:
    ligne.strip('e')

    print(ligne)
    fichier.close