temperaturas = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
for i in range(12):
    temperatura = float(input(f"Digite a temperatura média do mês de {meses[i]}: "))
    temperaturas.append(temperatura)

media_anual = sum(temperaturas) / len(temperaturas)
print("Temperaturas acima da média anual:")
for i, temperatura in enumerate(temperaturas):
    if temperatura > media_anual:
        print(f"{meses[i]}: {temperatura}")