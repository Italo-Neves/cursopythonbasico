'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol.
no odem de colocação. depois mostre:
- Os 5 primeiros
- Os últimos colocados.
- Times em ordem alfabetica
- Em qu posição está o time da chapecoense
'''


















# -*- coding: utf-8 -*-
time = ('Corinthias','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo','Vasco','Chapecoence','Atletico','Botafogo','Atlético-PR','Bahia','São Paulo','Fluminense','Sport Recife','EC Vitoria','Coritba','Avaí','Ponte Preta','Atletico-GO')
print(f'\n Lista dos times do brasileirão: {time}')
print(f'\n Os 5 primeiros times do brasileirão são: {time[:5]}')
print(f'\n Os 4 últimos times do brasileirão são: {time[-4:]}')
print(f'\n Lista dos times do brasileirão em ordem alfabética: {sorted(time)}')