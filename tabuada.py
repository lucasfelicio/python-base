#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10."""

__version__ = "0.1.0"
__author__ = "Lucas Felício"

#numeros = [1,2,3,4,5,6,7,8,9,10]

numeros = list(range(1,11))

# Interable (percorrivel)
for numero in numeros:
    print("Tabuada do: ", numero)
    for numero_multiplicado in numeros:
        print(numero * numero_multiplicado)
    print('------------')
