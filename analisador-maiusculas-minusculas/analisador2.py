#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 05:46:45 2020

@author: alexcosta
"""


entrada = input('Frase: ')
up = entrada.isupper()
low = entrada.islower()

if up:
    print(entrada.lower())
elif low:
    print(entrada.upper()) 
else:
    print(entrada.upper())
    print(entrada.lower())
