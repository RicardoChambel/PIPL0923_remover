numeros = [int(input(f"Digite o número {i+1}: ")) for i in range(5)]

soma = sum(numeros)

multiplicacao = 1

for num in numeros:

    multiplicacao *= num

print(f"Soma: {soma}")

print(f"Multiplicação: {multiplicacao}")

print(f"Números: {numeros}")