# ---------------- AULA 3 ---------------- 08 / 10 / 2024

from time import time

tp1 = ("Gonçalo", "ATEC", 10793)
print(tp1)

print(tp1[0])
print(tp1[1])
print(tp1[2])

#print(tp1[3]) <- ERRO


list_temp = list(tp1)
print(list_temp)

print("--- Unpack ---")

tp2 = ("Gonçalo", "ATEC", 10793)
nome, escola, UFCD = tp2

print(nome)
print(escola)
print(UFCD)

nome = "Novo Nome 2"

tp1 = ("Gonçalo","ATEC", 10793)
temp_list = list(tp1)
print(type(temp_list))
(nome, escola, UFCD) = temp_list

print(nome)
print(escola)
print(UFCD)

print("--- Metodo Tuple ---")
tp1 = ("Gonçalo","ATEC", 10793, "Gonçalo")
print(tp1.count("Gonçalo"))

# listas (array)
my_list = ["Gonçalo", "Ana", "Rita", "Luis"]

print(my_list)
print(my_list[0])
print(my_list[1])

my_list[0] = "Novo Nome"
print(my_list[0])
print(my_list)

nomes = [    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia",    "Karla", "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro", "Quintino", "Rafael", "Sara", "Tatiana",    "Ursula", "Vinicius", "Wagner", "Xavier", "Yasmin"]

print(nomes[0])

print(nomes[0:5]) # nomes[n:m] -> n a m-1

print(nomes[6:10]) #nomes[n:m] -> n a m-1

print(nomes[-10: -5])


print(nomes[0:20:3])

nomes.append("Rita")
print(nomes)


nomes.append("Aaron")
print(nomes[-1])

print("insert")
print(nomes[0:4])
nomes.insert(1, "Novo nome")
print(nomes[0:4])

print("remove")

nomes.remove("Novo nome")
print(nomes[0:4])


print(nomes[7])
print(nomes.pop(7))
print(nomes[7])

#print(nomes.remove("Outro nome"))
#print(nomes.pop(70))
#print("For array")

for nome in nomes:
    print(nome)

#receba 5 valores como input e adicione esses valores a uma lista
#mostre o conteudo da lista 
print("-------"* 10)
nova_lista = ["um", "dois", "tres", "quatro", "cinco"]

for i in range(5):
    novos = input("Digite um valor: ")
    nova_lista.append(novos)

print("\nLista com os valores adicionados: ")
print(nova_lista)


#receba N valores como input e adicione esses valores a uma lista
#mostre o conteudo de lista
#deve perguntar ao utilizador quando valores pretende adicionar
print("-------"* 10)
lista = []

n = int(input("Quantos valores você deseja adicionar à lista? "))

for i in range(n):
    valor = input(f"Digite o valor {i + 1}: ")
    lista.append(valor)

print("Conteúdo da lista:", lista)

#Faça um Programa que leia 20 numeros inteiros e armazene-os numa lista
#Armazene os numeros pares na lista PAR e os numeros IMPARES na lista impar
#Imprima os 3 vetores

print("------" * 10)
numeros = []
PAR = []
IMPAR= []

for i in range(20):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(num)

    if num % 2 == 0:
        PAR.append(num)
    else:
        IMPAR.append(num)

print("Lista de números:", numeros)
print("Lista de números pares:", PAR)
print("Lista de números ímpares:", IMPAR)



#receba N notas (0 a 20) como input e adicione esses valores a uma lista
#mostre o conteudo de lista
#deve perguntar ao utilizador quando valores pretende adicionar
#deve garantir que todas as notas sao validas
#deve assumir que o utilizador vai tentar adicionar valores numericos

'''
#Faça um Programa que leia 20 numeros inteiros e armazene-os numa lista
#Armazene os numeros pares na lista PAR e os numeros IMPARES na lista impar
#Imprima os 3 vetores
lista = [1,3,3,1,123,31,23,1234,54,6,25,1,4,42,5,62,4,134,414,3,45,1,413,234,532]

par = [ n for n in lista if n % 2 == 0]
impares = [ n for n in lista if n % 2 != 0]

print(f"par : {par}")
print(f"Impares: {impares}")
'''


num = int(input("Numeros de notas:"))
lista = []

for i in range(num):
    while True:
        nota = float(input(f"nota {i+1} (0 a 20): "))
        if 0 <= nota <= 20:
            lista.append(nota)
            break
        else:
            print("Nota inválida. Inserir um valor de 0 a 20")

for n in lista:
    print(f"{n:.2f}")

nomes = [
    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia", 
         "Karla", "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro", "Quintino", "Rafael", "Sara", "Tatiana",
         "Ursula", "Vinicius", "Wagner", "Xavier", "Yasmin" 
]


#Lista de nomes que terminam com "a"

lista2 = []

for nome in nomes:
    if nome[-1] == "a":
        lista2.append(nome)

print(lista2)

print("------------")

lista3 = [ n for n in nomes if n[-1] == "a"]

print(f"Lista 3: {lista3}")

lista3 = [len(n) for n in nomes if n[-1] == "a"]

print(f"Lista 3: {lista3}")
 
 
print("---------")
print("---------")
 
nomes.sort(reverse=True)
 
print(nome)
 
nomes2 = nomes
 
print(nomes2[0])
print(nomes[0])
 
nomes2[0] = "Novo nome"
 
print(nomes2[0])
print(nomes[0])

lista = list()

listNum = set()
    
    
