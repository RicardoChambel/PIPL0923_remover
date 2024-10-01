print("Ola Mundo")

#var

nome = "Valor" #String
idade = 10 # max int em c -> 2,147,483,647, max int cm Py -> não existe
nota = 10.9 # Flaot( 6 a 7) e Double (14)
aprovado = True #

print(nome)
nome = 10
print(nome)

soma = idade + 3
print(soma)

soma2 = nota + 2
print(soma2)

nome = "Valor"
soma3 = nome + " Foo"
print(soma3)

nome = "Valor"
#soma4 = nome + 2024
#print(soma4)

op5 = nome * 2
print(op5)

#print v2

nome = "Ricardo"
ano = 2024

#"Ola Mundo, Ricardo em 2024"

print("Ola Mundo, " + nome + " em " + str (ano))

print("Ola Mundo,", nome , "em", str(ano))

print(f"Ola Mundo, {nome.upper()} em {ano}")

""""
-> % <-
"""
op2 = 10 % 3
print(op2)

op2 = 12 % 3
print(op2)

op2 = 10 / 3
print(op2)

op2 = 10 // 3
print(op2)

#ler dados do teclado

nome2 = input("Ditie seu nome: ")
print(f"ola, {nome2}")

#Ifs
idade = 10

if (idade > 18):
    print("adulto")

print("Fora do if")

#Faça um programa que peça 2 numeros e imprima a soma
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2

print("A soma dos dois números é:", soma)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

print("A média das notas e:", (nota1 + nota2 + nota3 + nota4) / 4)

print("1. Faça um programa que converta metreos em centimetros")
metro = int(input("\tInsira um valor em metros:\n\t-> "))
print(f"\tValor em centímetros: {metro*100}")

print("2. Faça um programa que peça o raio de um círculo e de seguida seguida mostre a sua área")
raio = float(input("\tInsira o raio do círculo:\n\t-> "))
print(f"\tÁrea do círculo: {3.14*(raio*raio)}")

print("3. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.")
areaQuadrado = 4*4
print(f"\tÁrea do quadrado: {areaQuadrado}")
print(f"\tDobro desta área: {areaQuadrado*2}")

print("4. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.")
ganha = float(input("\tInsira quanto ganha por hora:\n\t-> "))
horas = float(input("\tInsira quantas horas trabalhou:\n\t-> "))
print(f"\tSalário: {ganha*horas}")

print("5. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).")
F = float(input("\tInsira a temperatura em graus Fahrenheit:\n\t-> "))
print(f"\tTemepratura em graus Celsius: {5*((F-32) / 9)}")

print("6. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.")
C = float(input("\tInsira a temperatura em graus Celsius:\n\t-> "))
print(f"\tTemperatura em Fahrenheit: {5*((C+32) / 9)}")

print("7. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:")
n1 = int(input("\tNumero 1:\n\t-> "))
n2 = int(input("\tNumero 2:\n\t-> "))
print(f"")