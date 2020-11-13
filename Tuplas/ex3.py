'''
Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números
gerados e também indique o menor e o maior valor que estão na tupla.
'''





















# -*- coding: utf-8 -*-
from random import randint
n = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f'Os números sorteados foram: {n}')
print(f'O maior valor gerado foi: {max(n)}')
print(f'O menor valor gerado foi: {min(n)}')