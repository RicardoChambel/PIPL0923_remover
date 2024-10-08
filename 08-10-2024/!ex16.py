salarios = [0] * 9
vendedores = int(input("Digite o número de vendedores: "))
for i in range(vendedores):
    salario = float(input(f"Digite o salário do vendedor {i+1}: "))
    indice = min(8, (salario - 200) // 100)
    salarios[indice] += 1

print("Intervalos de salários:")
for i, salario in enumerate(salarios):
    if i == 0:
        print(f"$200 - $299: {salario}")
    elif i == 1:
        print(f"$300 - $399: {salario}")
    elif i == 2:
        print(f"$400 - $499: {salario}")
    elif i == 3:
        print(f"$500 - $599: {salario}")
    elif i == 4:
        print(f"$600 - $699: {salario}")
    elif i == 5:
        print(f"$700 - $799: {salario}")
    elif i == 6:
        print(f"$800 - $899: {salario}")
    elif i == 7:
        print(f"$900 - $999: {salario}")
    elif i == 8:
        print(f"$1000 em diante: {salario}")