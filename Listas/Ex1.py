'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e
qual foi o menor valor digitado e as respectivas posições na lista.
'''





















n1 = []
maior = 0
menor = 999999
for num in range(0,5):
    n = int(input(f'Digite um valor para a posição {num}: '))
    n1.append(n)
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f' Você digitou: {n1}')
print(f' O maior número foi: {maior} nas posições ',end='')
for i, v in enumerate(n1):
    if v == maior:
        print(f'{i}...',end='')
print()
print( f' O menor número foi: {menor} nas posições ',end='')
for i, v in enumerate(n1):
    if v == menor:
        print(f'{i}...',end='')
print()
