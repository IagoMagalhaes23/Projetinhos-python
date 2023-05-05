"""
    Programa gerador de senhas
    Descrição:
        - Gera senhas de 8 digitos
        - Baseado na tabela ASCII
        - 1° digito é uma letra maiuscula
        - 2° digito é uma letra minuscula
        - 3° ao 7° digito são números
        - 8° digito é um caractere especial
    Exemplo:
        'D k 7 0 7 3 7 $'
"""

import random

letra_maiuscula = chr(random.randint(65,90))
letra_minuscula = chr(random.randint(97,122))
char_especial = chr(random.randint(33,38))
lista_numeros = []

for i in range(5):
    numeros = random.randrange(9)
    lista_numeros.append(numeros)

random.shuffle(lista_numeros)
lista_numeros = str(lista_numeros) [1:-1]
lista_numeros = lista_numeros.replace(',', '')

senha = letra_maiuscula + letra_minuscula + lista_numeros + char_especial
print(senha)