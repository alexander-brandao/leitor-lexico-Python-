# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""" 


from re import sub

entrada = input('Frase: ')
entrada = sub('(\/\*).*(\*\/)|(\/\/).*','',entrada)
print(entrada)
