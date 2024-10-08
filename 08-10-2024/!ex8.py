idades = []
alturas = []

for i in range(5):
    idade = int(input(f"Idade da pessoa {i+1}: "))
    altura = float(input(f"Altura da pessoa {i+1}: "))
    idades.append(idade)
    alturas.append(altura)

print("Idades [ reversed ]:")
idades.sort(reverse=True)
for idade in idades:
    print(idade)

print("Alturas [ reversed ]:")
alturas.sort(reverse=True)
for altura in alturas:
    print(altura)