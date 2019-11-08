#!/usr/bin/python3


fd = open('file.txt', 'r')
n = 0
for line in fd:
    n += 1

print (n)