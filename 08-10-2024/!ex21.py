carros = []
consumos = []
for i in range(5):
    modelo = input(f"Digite o modelo do carro {i+1}: ")
    consumo = float(input(f"Digite o consumo do carro {i+1} (km/l): "))
    carros.append(modelo)
    consumos.append(consumo)

menor_consumo = min(consumos)
melhor_carro = carros[consumos.index(menor_consumo)]

print("Comparativo de Consumo de Combustível")
print("----------------------------------------")
for i, (carro, consumo) in enumerate(zip(carros, consumos)):
    print(f"Veículo {i+1}")
    print(f"Nome: {carro}")
    print(f"Km por litro: {consumo:.2f}")

print("Relatório Final")
print("----------------")
for i, (carro, consumo) in enumerate(zip(carros, consumos)):
    litros = 1000 / consumo
    custo = litros * 2.25
    print(f"{i+1} - {carro} - {consumo:.2f} - {litros:.2f} litros - R${custo:.2f}")

print(f"O menor consumo é do {melhor_carro}.")