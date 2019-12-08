#!/usr/bin/python3
import os
import datetime
import sys
from datetime import timedelta

def sla(argument):
   calcul =( (365.25*24*3600*1 - 365.25*24*3600*argument/100) )
   print()
   affichage = datetime.timedelta( 0, calcul)
   return affichage



if __name__ == '__main__':
    print( sla( float(sys.argv[1])) )