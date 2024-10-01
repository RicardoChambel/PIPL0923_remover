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