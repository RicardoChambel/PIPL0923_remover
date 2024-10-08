idades = []
alturas = []

for i in range(5):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    altura = float(input(f"Digite a altura da pessoa {i+1}: "))
    idades.append(idade)
    alturas.append(altura)


print("Idades na ordem inversa:")

for idade in reversed(idades):
    print(idade)

print("Alturas na ordem inversa:")

for altura in reversed(alturas):
    print(altura)