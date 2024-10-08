import random

resultados = [0] * 6
for _ in range(100):
    resultado = random.randint(1, 6)
    resultados[resultado - 1] += 1

print("Simulação de Lançamento de Dados")
print("---------------------------------")
for i, resultado in enumerate(resultados):
    print(f"{i+1}: {resultado} ({resultado / 100 * 100:.2f}%)")