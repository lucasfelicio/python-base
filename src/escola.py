#!/usr/bin/env python3
"""Módulode exibição de relatório de crianças por atividades

Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades.
"""

__version__ = "0.1.1"

sala_1 = ['Erik', 'Lucas', 'Gustavo','Luan','Vitória'] 
sala_2 = ['Joao', 'Joana', 'Carlos','Isolda','Vitoria'] 

aula_ingles = ['Erik','Luan','Vitória', 'Carlos','Isolda']
aula_musica = ['Erik', 'Lucas', 'Gustavo','Luan','Vitória','Joao', 'Joana', 'Carlos','Isolda','Vitoria']
aual_danca = ['Joao', 'Joana', 'Gustavo'] 

atividades = [('Inglês', aula_ingles), 
              ('Música', aula_musica), 
              ('Dança', aual_danca)]

for label, atividade in atividades:
    print(f'Alunos da atividade {label}:\n')
    
    atividade_sala1 = set(sala_1) & set(atividade)
    atividade_sala2 = set(sala_2).intersection((atividade))
    
    print('Sala 1:', atividade_sala1)
    print('Sala 2:', atividade_sala2)
    print("-" * 30)