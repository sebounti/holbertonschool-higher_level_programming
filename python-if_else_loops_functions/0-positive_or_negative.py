#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
        print( number, 'is positif')
elif number < 0:
        print( number, 'is negatif')
else :
        print( number, 'is zero')