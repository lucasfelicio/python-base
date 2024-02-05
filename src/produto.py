#! /usr/bin/env python3
"""Cadastro de produto."""

__version__ = '0.1.0'

produto = {
    "nome": "Caneta",
    "cores": ["Azul","Vermenlha"],
    "preco": 5.99,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8
    },
    "em_estoque": True,
    "codigo": 9872421,
    "codebar": None
}

compra = ("Lucas", produto["nome"], 4)

total_compra = compra[2] * produto["preco"]

print(f"O cliente {compra[0]} comprou {compra[2]} {compra[1]} e pagou um total de R$ {total_compra}")