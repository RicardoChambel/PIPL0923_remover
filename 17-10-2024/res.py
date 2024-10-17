import random

class Quadrado:
    def __init__(self, lado: int, cor: str):
        self.lado = lado
        self.cor = cor
    
    def area(self):
        area = self.lado * self.lado
        return area

q = []
for _ in range(400):
    q.append(Quadrado(random.randint(1, 20), "Cor"))

areas = [quadrado.area() for quadrado in q]

maior_area = areas[0]
menor_area = areas[0]
indice_maior_area = 0
indice_menor_area = 0

for i in range(1, len(areas)):
    if areas[i] > maior_area:
        maior_area = areas[i]
        indice_maior_area = i
    if areas[i] < menor_area:
        menor_area = areas[i]
        indice_menor_area = i

print(f"\nO Quadrado {indice_maior_area + 1} tem a maior área: {maior_area}")
print(f"O Quadrado {indice_menor_area + 1} tem a menor área: {menor_area}")