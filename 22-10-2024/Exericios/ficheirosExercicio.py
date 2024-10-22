nome = input("Insira o seu nome: ")
idade = input("Insira a sua idade: ")
email = input("Insira o seu email: ")

try:
    ficheiro = open("dados.txt", "a")
    ficheiro.write("- Dados -\n")
    ficheiro.write(f"Nome: {nome}\nIdade: {idade}\nEmail: {email}\n\n")
    ficheiro.close()
    print("Dados salvos no ficheiro \"dados.txt\"")
except Exception as e:
    print("Ocorreu um erro ao salvar os dados")
    print(f"Erro:{e}")