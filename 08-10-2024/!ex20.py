salarios = []
while True:
    salario = float(input("Digite o salário do colaborador (ou 0 para encerrar): "))
    if salario == 0:
        break
    salarios.append(salario)

total_abono = 0
contagem_minimo = 0
maior_abono = 0
for salario in salarios:
    abono = max(100, salario * 0.2)
    total_abono += abono
    if abono == 100:
        contagem_minimo += 1
    if abono > maior_abono:
        maior_abono = abono

print("Projeção de Gastos com Abono")
print("-------------------------------")
for i, salario in enumerate(salarios):
    abono = max(100, salario * 0.2)
    print(f"Salário: R${salario:.2f} - Abono: R${abono:.2f}")

print(f"Foram processados {len(salarios)} colaboradores")
print(f"Total gasto com abonos: R${total_abono:.2f}")
print(f"Valor mínimo pago a {contagem_minimo} colaboradores")
print(f"Maior valor de abono pago: R${maior_abono:.2f}")