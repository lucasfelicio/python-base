#! /usr/bin/env python3
"""
Hello World Multi linguas.

Dependendo da lingua configurada, o programa vai imprimir o texto
de acordo com a lingua.

Como usar:

Tenha a variável LANG configurada com a linguagem que deseja. Ex:

    export LANG=pt

Execução:

    python3 hello.py ou ./hello.py
"""
__version__ = '0.1.2'
__author__ = 'Lucas Felício'
__license__ = 'Unlicense'

import os

current_language = os.getenv('LANG', 'en_US').split('.')[0]

# msg = 'Hello, World'

# if current_language == 'en_US':
#     msg = 'Hello, World'
# elif current_language == 'pt_BR':
#     msg = 'Olá, Mundo'
# elif current_language == 'es_ES':
#     msg = 'Hola Mundo'
# elif current_language == 'zh_CN':
#     msg = '你好，世界'
# elif current_language == 'it_IT':
#     msg = 'Ciao, Mondo'
# elif current_language == 'fr_FR':
#     msg = 'Bonjour, Monde'
# elif current_language == 'ja_JP':
#     msg = 'こんにちは、世界'
# elif current_language == 'ko_KR':
#     msg = '안녕하세요, 미래'
# elif current_language == 'ru_RU':
#     msg = 'Привет, Мир'
# elif current_language == 'tr_TR':
#     msg = 'Merhaba, Dünya'

# print(msg)

msg = {
    'en_US': 'Hello, World',
    'pt_BR': 'Olá, Mundo',
    'es_ES': 'Hola Mundo',
    'fr_FR': 'Bonjour, Monde'
}

print(msg[current_language])