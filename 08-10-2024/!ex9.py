numeros = [int(input(f"Digite o número {i+1}: ")) for i in range(10)]

soma_quadrados = sum(num ** 2 for num in numeros)

print(f"Soma dos quadrados: {soma_quadrados}")