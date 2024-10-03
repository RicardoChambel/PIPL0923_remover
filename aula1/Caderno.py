# CADERNO RICARDO CHAMBEL

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

#Condições / Controlo de fluxo

#boolean (True | False)
'''
E (os dois têm de ser verdadeiros)
T e T -> T
T e F -> F
F e T -> T
F e F -> F

OU (qualquer um pode ser verdadeiro)
T ou T -> T
T ou F -> T
F ou T -> T
F ou F -> F

XOU (apenas um pode ser verdadeiro)
T xou T -> F
T xou F -> T
F xou T -> T
F xou F -> F
'''

ano = 2024


#------- if's (se) -------:

if ano == 2024:
        print("ano = 2024")
else:
    print("Outro ano")

    print("fora do if")

#Faça um programa que peça dois númros e imprima o maior deles

nmr1 = float(input("Digite um numero"))
nmr2 = float(input("digite outro numero: "))

if nmr1 > nmr2:
    print(f"O {nmr1} é > que o {nmr2}")
else:
    print(f"O {nmr2} é > que o {nmr1}")




# else if ( se não se )
# else ( se não)
# switch ( escolha )

# ------- loops -------
#for (para)
#while ( enquanto - faça)