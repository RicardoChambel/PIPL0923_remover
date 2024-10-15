dicionariodinamico = {}

num_entradas = int(input("Quantas entradas deseja adicionar? "))

for _ in range(num_entradas):
    chave = input("Digite a chave: ")
    valor = input("Digite o valor: ")
    dicionariodinamico[chave] = valor


print("O dicionário final é:", dicionariodinamico)