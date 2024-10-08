def bytes_para_megabytes(bytes):
    return bytes / (1024 * 1024)

def calcular_percentual(valor, total):
    return (valor / total) * 100

usuarios = []
with open("usuarios.txt", "r") as arquivo:
    for linha in arquivo:
        nome, bytes = linha.strip().split()
        usuarios.append((nome, int(bytes)))

total_bytes = sum(bytes for _, bytes in usuarios)
media_bytes = total_bytes / len(usuarios)

print("ACME Inc.               Uso do espaço em disco pelos usuários")
print("------------------------------------------------------------------------")
print("Nr.  Usuário        Espaço utilizado     % do uso")
for i, (nome, bytes) in enumerate(usuarios):
    megabytes = bytes_para_megabytes(bytes)
    percentual = calcular_percentual(bytes, total_bytes)
    print(f"{i+1}    {nome}           {megabytes:.2f} MB             {percentual:.2f}%")

print(f"Espaço total ocupado: {bytes_para_megabytes(total_bytes):.2f} MB")
print(f"Espaço médio ocupado: {media_bytes:.2f} MB")

with open("relatorio.txt", "w") as arquivo:
    arquivo.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
    arquivo.write("------------------------------------------------------------------------\n")
    arquivo.write("Nr.  Usuário        Espaço utilizado     % do uso\n")
    for i, (nome, bytes) in enumerate(usuarios):
        megabytes = bytes_para_megabytes(bytes)
        percentual = calcular_percentual(bytes, total_bytes)
        arquivo.write(f"{i+1}    {nome}           {megabytes:.2f} MB             {percentual:.2f}%\n")
    arquivo.write(f"Espaço total ocupado: {bytes_para_megabytes(total_bytes):.2f} MB\n")
    arquivo.write(f"Espaço médio ocupado: {media_bytes:.2f} MB\n")