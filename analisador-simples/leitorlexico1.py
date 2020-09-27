#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 22:42:13 2020

@author: alexcosta
"""


entrada = input('Frase: ')
semespaco = entrada.replace(" ","")
cont = entrada.count(" ")
print("Total de caracteres: ", len(entrada))
print("Espacos em branco: ", (cont))
print(semespaco) 