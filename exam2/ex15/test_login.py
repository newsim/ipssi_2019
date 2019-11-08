#!/usr/bin/python3

# -*- coding: utf-8 -*-

import sys
import time


import hashlib

print(sys.argv[1])
print(hashlib.md5(sys.argv[1].encode('utf-8')).hexdigest())