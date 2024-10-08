
# ---------------- AULA 2 ---------------- 03 / 10 / 2024

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
    print("\tDentro do if")
    print("\tano = 2024")
else:
    print("\tDentro do else")
    print("\tOutro ano")
print("Fora do if")


print("--" * 10)

#Faça um programa que peça dois númros e imprima o maior deles

nmr1 = float(input("\tDigite um numero: "))
nmr2 = float(input("\tdigite outro numero: "))

if nmr1 > nmr2:
    print(f"\t{nmr1}")
else:
    print(f"\t{nmr2}")


print("--" * 10)

num = 5
print(f"\tNúmero: {num}")

if num % 2 == 0 and num % 5 == 0:
    print("\tResultado: Par e div por 5")
else:
    print("\tResultado: Impar ou nao div por 5")


'''
== <- Comaprações
= <- Atribuição
'''

print("--" * 10)

##################################### PROGRAMA ######################################
## faça um programa que verifique se uma letra digitada é "F" ou "f" ou "M" ou "m" ##

letra = input("\tInsira uma letra:")
if letra == "F" or letra == "f" or letra == "M" or letra == "m":
    if letra == "F" or letra == "f":
        print("\tFeminino")
    if letra == "M" or letra == "m":
        print("\tMasculino")
else:
    print("\tGenero Inválido")

print("--" * 10)

# switch ( escolha )
num =5
print(f"Numero: {num}")
match num:
    case 0:
        print(f"\tCase 0")
        print("\tO num e 0")
    
    case 1:
        print(f"\tCase 1")
        print("\tO num e 1")
    
    case 5:
        print(f"\tCase 5")
        print("\tO num e 5")
        
    case _:
        print(f"\tCase _")
        print("\toutro valor")


print("--" * 10)

menu = """
############ Menu ############
# OP1 ............ 1 #
# OP2 ............ 2 #
# OP3 ............ 3 #

 ########################"""
print(menu)

op = input("\tSelecione a op:")

match op:
    case "1":
        print(f"\tCase 1")
        print("\tO num e 1")
    
    case "2":
        print(f"\tCase 2")
        print("\tO num e 2")
    
    case "3":
        print(f"\tCase 3")
        print("\tO num e 3")
        
    case _:
        print(f"\tCase _")
        print("\tOutro valor")


print("--" * 10)

#loops

#for (par)

#while ( enquanto - faça)
count = 0
while op != "q":
    print(f"\tLoop: {count}")
    
    op = input("\tInsira o valor 'q': ")
    
    count += 1

print("--" * 10)
num = 0

while num < 10:
    print(num)
    num += 1

'''
num++
v
num = num + 1

num += 4
v
num = num + 4

num *= 4
v
num = num * 4


num -= 4
v
num = num - 4
'''

range(0, 10, 2)
'''
range(a, b, c)

a- LB
b- UP
c- step, se oculto: c = 1

range(1, 5)
R: 1, 2, 3, 4

range(5)
R: 0, 1, 2, 3, 4

range(0, 10, 2)
0, 2, 4, 6, 8
'''

# else if ( se não se )
# else ( se não)
# switch ( escolha )

# ------- loops -------
#for (para)

print("--" * 10)

for elm in range(0, 100):
    print(elm)
    if elm % 2 == 50:
        break


print("--" * 10)

nomes = ["Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia", "Karla", "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro", "Quintino", "Rafael", "Sara", "Tatiana", "Ursula", "Vinicius", "Wagner", "Xavier", "Yasmin"]
print("Nomes:")

for nome in nomes:
    print("\t•",nome)
    
print("--" * 10)
print("Daniela: - ",nomes.count("Daniela"))

print("--" * 10)
print("Tamanho da lista: ",nomes.__len__())

print("--" * 10)
print("Tamanho da lista: ",len(nomes))

print("--" * 10)
print("Sara na lista: ",nomes.__contains__("Sara"))
print("Ana na lista: ",nomes.__contains__("Ana"))
print("Pedro na lista: ", "Pedro" in nomes)

print("--" * 10)
print("Nomes | .sort(reverse=True)")

nomes.sort(reverse=True)
print("\t",nomes, "\n")
    
print("--" * 10)
print("Nomes | .sort")

nomes.sort()
print("\t",nomes, "\n")

#while ( enquanto - faça)


'''

var
tipos de dados
type cast - int("..."), srt(...)
tuplos
op com var
if
elif
else
and / or
match
while
for
list

'''

#################### PROGRAMA ####################
### Faça um programa que peça uma nota, entre zero e dez.Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. ###
print("--" * 10)
while True:
    try:
        nota = int(input('Insira um nota de 0-10: '))
        if nota >= 0 and nota <=10:
            break
        else:
            print("Nota inválida")
    except ValueError:
            print("Valor inválido")