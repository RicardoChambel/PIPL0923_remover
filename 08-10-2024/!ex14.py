respostas = []
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
for i, pergunta in enumerate(perguntas):
    resposta = input(pergunta).lower()
    while resposta not in ["sim", "não"]:
        resposta = input("Resposta inválida. Por favor, digite 'sim' ou 'não': ").lower()
    respostas.append(resposta)

contagem = sum(1 for resposta in respostas if resposta == "sim")
if contagem == 2:
    print("Suspeita")
elif contagem >= 3 and contagem <= 4:
    print("Cúmplice")
elif contagem == 5:
    print("Assassino")
else:
    print("Inocente")