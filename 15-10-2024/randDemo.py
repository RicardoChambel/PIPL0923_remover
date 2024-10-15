import random

print(random.randint(1,10000))

# Crie uma lista com 1000 números inteiros aleatorios
# Imprima o valor todos os valores da lista multiplicacao pela posição
# Exemplo:
#Lista -> [3,4,5,10]
# output:
# 0
# 4
# 10
# 30

lista = []
for _ in range(1000):
    num = random.randint(1,1000)
    lista.append(num)

print("Indice | Numero*Indice: (resultado)")
mult = 0
for _ in lista:
    print(f"{mult} | {lista[mult]}*{mult}: {mult * lista[mult]}")
    mult += 1