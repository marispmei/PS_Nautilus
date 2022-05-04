'''
3-
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''
total = 200
coins = [1, 2, 5, 10, 50, 100, 200]
possibilidades = [1] + [0]*total
for moeda in coins:
    for i in range(moeda,total+1):
        possibilidades[i] += possibilidades[i-moeda]

print(possibilidades[total])
