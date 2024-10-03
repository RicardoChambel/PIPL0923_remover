import os
def limpar():
    os.system("cls")
def next():
    print("--"*10)
    input("Enter para continuar")

# EXERCICIO 1 --------------------------------------------------------------------------------
# Feito no caderno

# Exercicio 2 --------------------------------------------------------------------------------
# Feito no caderno

# Exercicio 3 --------------------------------------------------------------------------------
# Feito no caderno

# Exercicio 4 --------------------------------------------------------------------------------
limpar()

print("4. Vogal ou Consoante")
letra = input("Insira uma letra: ")
letra.lower()
if letra in ["a", "e", "i", "o", "u"]:
    print("A letra é uma vogal")
else:
    print("A letra é uma consoante")
    
next()

# Exericio 5 --------------------------------------------------------------------------------
limpar()

print("5. Calcular média")
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
if (nota1+nota2)/2>=7:
    print("Aluno aprovado [Média: {media}]")
elif (nota1+nota2)/2<7:
    print("Aluno reprovado")
elif (nota1+nota2)/2==10:
    print("Aprovado com Distinção")
next()

# Exercicio 6 --------------------------------------------------------------------------------
limpar()

print("6. Maior de 3")
n1 = float(input("Insira o primeiro numero: "))
n2 = float(input("Insira o segundo numero: "))
n3 = float(input("Insira o terceiro numero: "))
if n1 > n2 and n1 > n3: print(n1)
elif n2 > n1 and n2 > n3: print(n2)
elif n3 > n1 and n3 > n2: print(n3)
else:print(n1)

next()

# Exericio 7 --------------------------------------------------------------------------------
limpar()

print("7. Maior e menor de 3")
n1 = float(input("Insira o primeiro numero: "))
n2 = float(input("Insira o segundo numero: "))
n3 = float(input("Insira o terceiro numero: "))
if n1 > n2 and n1 > n3: print("Numero maior: ",n1)
elif n2 > n1 and n2 > n3: print("Numero maior: ",n2)
elif n3 > n1 and n3 > n2: print("Numero maior: ",n3)
if n1 < n2 and n1 < n3: print("Numero menor: ",n1)
elif n2 < n1 and n2 < n3: print("Numero menor: ",n2)
elif n3 < n1 and n3 < n2: print("Numero menor: ",n3)
else:print("Numero maior e menor: ",n1)

next()

# Exericio 8 --------------------------------------------------------------------------------
limpar()

print("8. Preço barato")
n1 = float(input("Insira o preço do primeiro produto: "))
n2 = float(input("Insira o segundo preço: "))
n3 = float(input("Insira o terceiro preço: "))
if n1 < n2 and n1 < n3: print("Deve comprar o primeiro produto.")
elif n2 < n1 and n2 < n3: print("Deve comprar o segundo produto.")
elif n3 < n1 and n3 < n2: print("Deve comprar o terceiro produto.")
else:print("Pode comprar qualquer um.")


next()

# Exericio 9 --------------------------------------------------------------------------------
limpar()

print("9. Ordem decrescente")
n1 = float(input("Insira o primeiro numero: "))
n2 = float(input("Insira o segundo numero: "))
n3 = float(input("Insira o terceiro numero: "))
lista = []
lista.append(n1)
lista.append(n2)
lista.append(n3)
lista.sort(reverse=True)
print("Lista em ordem decrescente: ", end="")
for i in lista:
    if i == len(lista)-1:
        print(i, end=".")
    else:
        print(i, end=", ")

next()

# Exericio 10 --------------------------------------------------------------------------------
limpar()

turno = input("Insira o seu turno (M, V, N): ")
if turno.lower == "m":print("Bom Dia!")
if turno.lower == "v":print("Boa Tarde!")
if turno.lower == "n":print("Boa Noite!")


