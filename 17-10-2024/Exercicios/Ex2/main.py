from quadrado import Quadrado
from triangulo import Triangulo
from trapezio import Trapezio
from circulo import Circulo

"""
q1 = Quadrado(20, "Amarelo")
print(q1.area())

q2 = Quadrado(34, "Azul")
"""

"""
Criar base para a class

triangulo
circulo
trapezio

"""
# Triangulos
t1 = Triangulo(20, 20, "Roxo")

t2 = Triangulo(34, 20, "Vermelho")

# Trapezios
t1 = Trapezio(20, 20, 20, "Preto")

t2 = Trapezio(34, 30, 20, "Branco")

# Circulo
t1 = Circulo(10, "Laranja")

t2 = Circulo(14, "Rosa")


"""
Crie 4 quadrados
Indique o que tem a maior area, não utilizar função max

"""
q1 = Quadrado(7, "Amarelo")
q2 = Quadrado(3, "Azul")
q3 = Quadrado(2, "Verde")
q4 = Quadrado(6, "Vermelho")

quadrados = [q1,q2,q3,q4]

q1_area = q1.area()
q2_area = q2.area()
q3_area = q3.area()
q4_area = q4.area()

quadrados_area = [q1_area,q2_area,q3_area,q4_area]

tamanho = 0
quadrado = 0
quadradoFinal = 0
for maior in quadrados_area:
    quadrado += 1
    if maior > tamanho:
        tamanho = maior
        print(maior)
        quadradoFinal = quadrado

print("\n")
print(f"Área do Quadrado 1 (Amarelo): {q1_area}")
print(f"Área do Quadrado 2 (Azul): {q2_area}")
print(f"Área do Quadrado 3 (Verde): {q3_area}")
print(f"Área do Quadrado 4 (Vermelho): {q4_area}")

print(f"\n-> O quadrado com a maior área é o quadrado  {quadradoFinal}, com área de {tamanho}\n")