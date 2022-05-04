'''
1-
CRIE UMA FUNÇÃO QUE REALIZE TANTO UMA PA QUANTO UMA PG PARA VALORES INTEIROS
SE A RAZÃO FOR PAR DEVERÁ SER REALIZADA UMA P.A DE TERMO N1 ATÉ UM VALOR X QUE NÃO DEVE SER ULTRAPASSADO
SE O VALOR DA RAZÃO FOR ÍMPAR A FUNÇÃO REALIZARA UMA PG

cada termo tanto da PA quanto da PG devem ser armazenados em uma lista 

exemplo 
n1= 2
nx= 13
razão = 4

output = [2, 6, 10]
'''

import math
def pa_pg():
    n1 = int(input("Valor inteiro: "))
    nx = int(input("Valor limite: "))
    razao = int(input("Razão: "))
    lista = []
    if razao%2==0:
        n_elementos = int(((nx-n1)/razao) + 1)
        n = n1 + (n_elementos-1)*razao
        for z in range(n1, nx, razao):
            lista.append(z)
    else:  
        n_elementos = int(math.log((nx/n1), razao) + 1)
        for nx in range(1, n_elementos + 1):
                    lista.append(n1 * razao ** (nx - 1))
    print(lista)
pa_pg()
