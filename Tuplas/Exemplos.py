'''
Tuplas são váriaveis compostas, que podem armazenar diversos valóres,
porém uma vez que uma tupla é criada ela é imutalvel!
'''




















lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')# --> as tuplas podem ser declaradas com o uso e parenteses
print(lanche) # --> para mostrar uma tupls inteira
#print(lanche[1]) #--> podemos selecionar um intém especifico da lista depois
#print(lanche[1:3]) #--> podemos fatiar uma tupla assim como fazemos com strings(lembre-se que o ultimo elemento sempre é ignorado!)
#print(lanche[2:])
#print(lanche[-2:])
#print(sorted(lanche))
















'''
Podemos usar uma tupla dentro de um looping como no exemplo abaixo:

for comida in lanche:
    print(f'eu vou comer {comida}')
print(f'No total comi:{len(lanche)} itens do cardápio!')
------------------------------------------------------------------------------------------------------------------------
for c in range(0, len(lanche)):
    print(f'O lanche {lanche[c]} é o itém {c} do cardapio')
------------------------------------------------------------------------------------------------------------------------
Podemos somar duas tuplas da seguinte maneira:

a = (2, 5, 4)
b = (5, 8, 1, 3)
c = a + b 
print(c)
print(c.count(5)) --> retorna quantas vezes a letra 5 aparece na tupla!
print(c.index(8)) --> retorna a posição do número 8

'''
