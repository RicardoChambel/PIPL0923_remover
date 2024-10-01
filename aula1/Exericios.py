# EXERCICIO 1 --------------------------------------------------------------------------------
print("1. Faça um Programa que mostre a mensagem \"Alo mundo\" na tela.")
print("\tAlo Mundo")

# EXERCICIO 2 --------------------------------------------------------------------------------
print("2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].")
nmr=float(input("\tInsira um numero:\n\t-> "))
print(f"\tO numero informado foi {nmr}")

# EXERCICIO 3 --------------------------------------------------------------------------------
print("3. Faça um programa que peça 2 numeros e imprima a soma")
num1 = float(input("\tDigite o primeiro número:b "))
num2 = float(input("\tDigite o segundo número: "))

soma = num1 + num2

# EXERCICIO 4 --------------------------------------------------------------------------------
print("4. A soma dos dois números é:", soma)

nota1 = float(input("\tDigite a primeira nota: "))
nota2 = float(input("\tDigite a segunda nota: "))
nota3 = float(input("\tDigite a terceira nota: "))
nota4 = float(input("\tDigite a quarta nota: "))

print("\tA média das notas e:", (nota1 + nota2 + nota3 + nota4) / 4)

# EXERCICIO 5 --------------------------------------------------------------------------------
print("5. Faça um programa que converta metreos em centimetros")
metro = int(input("\tInsira um valor em metros: "))
print(f"\tValor em centímetros: {metro*100}")

# EXERCICIO 6 --------------------------------------------------------------------------------
print("6. Faça um programa que peça o raio de um círculo e de seguida seguida mostre a sua área")
raio = float(input("\tInsira o raio do círculo: "))
print(f"\tÁrea do círculo: {3.14*(raio*raio)}")

# EXERCICIO 7 --------------------------------------------------------------------------------
print("7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.")
areaQuadrado = 4*4
print(f"\tÁrea do quadrado: {areaQuadrado}")
print(f"\tDobro desta área: {areaQuadrado*2}")

# EXERCICIO 8 --------------------------------------------------------------------------------
print("8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.")
ganha = float(input("\tInsira quanto ganha por hora: "))
horas = float(input("\tInsira quantas horas trabalhou: "))
print(f"\tSalário: {ganha*horas}")

# EXERCICIO 9 --------------------------------------------------------------------------------
print("9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).")
F = float(input("\tInsira a temperatura em graus Fahrenheit: "))
print(f"\tTemepratura em graus Celsius: {5*((F-32) / 9)}")

# EXERCICIO 10 --------------------------------------------------------------------------------
print("10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.")
C = float(input("\tInsira a temperatura em graus Celsius: "))
print(f"\tTemperatura em Fahrenheit: {5*((C+32) / 9)}")

# EXERCICIO 11 --------------------------------------------------------------------------------
print("11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:")
n1 = int(input("\tNumero inteiro 1: "))
n2 = int(input("\tNumero inteiro 2: "))
n3 = float(input("\tNumero real 2: "))
print(f"\tProduto do dobro do primeiro com metade do segundo: {(n1*2)*(n2/2)}")
print(f"\tSoma do triplo do primeiro com o terceiro: {(n1*3)+n3}")
print(f"\tTerceiro elevado ao cubo: {n3**3}")

# EXERCICIO 12 --------------------------------------------------------------------------------
print("8. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58")
altura = float(input('Altura:'))
print ('\tPeso ideal:', (72.7*altura) - 58)

# EXERCICIO 13 --------------------------------------------------------------------------------
print("""13. Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu 
peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 (h = altura)
Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso. """)

sexo = int(input('\tEscolha: 1- Sexo Masculino / 2- Sexo Feminino: '))
h = float(input('\tAltura:'))
peso = float(input('\tPeso:'))

peso_ideal = (72.7*h) - 58 if sexo == 1 else (62.1*h) - 44.7

if peso < peso_ideal:
	print('\tAbaixo do peso ideal!')
elif peso == peso_ideal:
	print('\tDentro do peso ideal!')
else:
	print('\tAcima do peso ideal!')
print ('\tPeso: %.2f / Peso ideal: %.2f' %(peso, peso_ideal))

# EXERCICIO 14 --------------------------------------------------------------------------------
print("""14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes 
maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa 
que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor 
da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.""")

peso = float(input('\tPeso:'))
if peso > 50:
	exc = peso - 50
	multa = exc * 4
else:
	exc = 0
	multa = 0
print ('\tPeso: %.2f Kg' %peso)
print ('\tExcesso: %.2f Kg' %exc)
print ('\tMulta: R$ %.2f' %multa)

# EXERCICIO 15 --------------------------------------------------------------------------------
print("""15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.""")

vh = float(input('\tValor da hora:'))
qh = int(input('\tQuantidade de horas trabalhadas:'))

salario_bruto = vh * qh
inss = 8/100 * salario_bruto
sindicato = 5/100 * salario_bruto
ir = 11/100 * salario_bruto

salario_liquido = salario_bruto - inss - sindicato - ir

print ('\t + Salário Bruto: R$ %.2f' %salario_bruto)
print ('\t - IR: R$ %.2f' %ir)
print ('\t - INSS: R$ %.2f' %inss)
print ('\t - Sindicato: R$ %.2f' %sindicato)
print ('\t = Salário Liquido: R$ %.2f' %salario_liquido)

# EXERCICIO 16 --------------------------------------------------------------------------------
print("""16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
      Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
      Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.""")

tamanhoMetro = float(input("\tInsira o tamanho em metros quadrados: "))

cobertura_por_litro = 3  # 1 litro cobre 3m quadrados
litros_por_lata = 18      # Cada lata contém 18
preco_por_lata = 80.00    # Cada lata custa 80

litros_necessarios = tamanhoMetro / cobertura_por_litro

latas_necessarias = -(-litros_necessarios // litros_por_lata)

custo_total = latas_necessarias * preco_por_lata

# Exibindo os resultados
print(f"\nQuantidade de latas de tinta a serem compradas: {int(latas_necessarias)}")
print(f"\tPreço total: R$ {custo_total:.2f}")

# EXERI9CIO 17 --------------------------------------------------------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# EXERCICIO 18 --------------------------------------------------------------------------------
print("""18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).""")

tamanho = float(input('\tTamanho do arquivo (MB): '))
velocidade = float(input('\tVelocidade de Internet (MBps): '))
print('\tTempo aproximado de download: %.0f Minutos ' %((tamanho / velocidade) * 60))