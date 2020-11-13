'''
Crie um programa onde o usuario pode digitar vários valores numéricos e cadastre-os em lista. caso o número já exista
lá dentro ele não será adicionado. No final serão exibidos todos os valores únicos digitados, em ordem crescente.
'''





















# -*- coding: utf-8 -*-
vetor = []
while True:
    n = int(input('Digite um numero: '))
    if n not in vetor:
      vetor.append(n)
    else:
      print('valor Duplicado não irei adicionar!!!')
    op = str(input('Deseja continuar? [S/N] ')).upper()
    if op == 'N':
      break
print(f'O vetor gerado foi: {sorted(vetor)}')
