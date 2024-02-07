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

cliente = {
    "nome": "Lucas"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 4
}

total_compra = compra['quantidade'] * produto["preco"]

print(
    f"O cliente {compra['cliente']['nome']} "  
    f"comprou {compra['quantidade']} {compra['produto']['nome']} "
    f"e pagou um total de R$ {total_compra}")