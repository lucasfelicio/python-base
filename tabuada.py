#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10."""

__version__ = "0.1.0"
__author__ = "Lucas Felício"

# Interable (percorrivel)
numeros = list(range(1,11))

for n1 in numeros: 
    print("{:-^18}".format(f"Taboada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("#" * 18)