# ---------------- AULA 3 ---------------- 08 / 10 / 2024

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




print(nomes.remove("Outro nome"))
print(nomes.pop(70))
print("For array")

for nome in nomes:
    print(nome)

# Receba 5 valores como input e adicione esses valores a uma lista
# Mostre o conteúdo da lista

valores = []
for i in range(5):
    valor = input("Digite um valor: ")
    valores.append(valor)

print("Conteúdo da lista:")
print(valores)

print("-------"* 10)
valores = [1, 2, 3, 4, 5]

n = int(input("Quantos valores deseja adicionar à lista? "))

for i in range(n):
    valor = input(f"Digite o valor {i + 1}: ")
    valores.append(valor)

print("Conteúdo da lista:", valores)

#Faça um Programa que leia 20 nuumeros inteiros e armazene-os numa lista
#Armazene os mumeros pares na lista Par e os numeros Impares na lista impar
#Imprima os 3 vetores

numeros = []
pares = []
impares = []

for i in range(20):
    num = int(input(f"Digite o {i + 1}º numero inteiro: "))
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Lista de números:", numeros)
print("Lista de números pares:", pares)
print("Lista de números ímpares:", impares)
