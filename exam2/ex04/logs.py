#!/usr/bin/python3
from datetime import datetime

def logthis(message):
    fichier = open("python.log", "a")
    fichier.write(datetime.now().strftime("%d/%m/%y %H:%M ") + message + "\n")
    fichier.close()