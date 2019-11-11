#!/usr/bin/python3

# -*- coding: utf-8 -*-

import sys
import time


import hashlib

a = sys.argv

if (hashlib.md5(sys.argv[1].encode('utf-8')).hexdigest()) == '82771f9740d5e024ab823c12a9b51289':
    print ('bon mot de passe')
else:
    print ('mauvais mot de passe')


""" def login(a):
    if (hashlib.md5(sys.argv[0].encode('utf-8')).hexdigest()) == '82771f9740d5e024ab823c12a9b51289':
        return print ('bon mot de passe')
    else:
        return print ('mauvais mot de passe') """