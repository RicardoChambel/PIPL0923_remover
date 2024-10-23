import os
 
def clear():
    os.system("cls")
 
class Aluno:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.aulas_inscritas = []
 
    def inscrever_aula(self, aula):
        if aula.horario in [aula.horario for aula in self.aulas_inscritas]:
            print("\n- Não pode se inscrever em mais de uma aula no mesmo horário! -")
            return False
 
        if len(aula.alunos_inscritos) >= aula.numero_max_alunos:
            print("\n- Aula já lotada! -")
            return False
 
        self.aulas_inscritas.append(aula)
        aula.inscrever_aluno(self)
        print(f"\n- {self.nome} inscrito na aula às {aula.horario}! -")
        return True
 
 
class Instrutor:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.aulas = []
        self.aula = None
 
    def adicionar_aula(self, aula):
        self.aula = aula
 
 
class Aula:
    def __init__(self, instrutor, horario, numero_max_alunos, duracao):
        self.instrutor = instrutor
        self.horario = horario
        self.numero_max_alunos = numero_max_alunos
        self.duracao = duracao
        self.alunos_inscritos = []
 
        instrutor.adicionar_aula(self)
 
    def inscrever_aluno(self, aluno):
        self.alunos_inscritos.append(aluno)
 
 
class Ginasio:
    def __init__(self):
        self.alunos = []
        self.instrutores = []
        self.aulas = []
        self.carregar_ficheiros()
 
    def carregar_ficheiros(self):            
        ficheiroAlunos= open("alunos.txt", "a")
        ficheiroAlunos.close()
        ficheiroInstrutores = open("instrutores.txt", "a")
        ficheiroInstrutores.close()
        ficheiroAulas = open("aulas.txt", "a")
        ficheiroAulas.close()
        try:
            ficheiroAlunos= open("alunos.txt", "r")
            ficheiroInstrutores = open("instrutores.txt", "r")
            ficheiroAulas = open("aulas.txt", "r")
            # Carregar Alunos
            for linha in ficheiroAlunos:
                nome, email = linha.strip().split(',')
                aluno = Aluno(nome, email)
                self.alunos.append(aluno)
            # Carregar Instrutores
            for linha in ficheiroInstrutores:
                nome, email = linha.strip().split(',')
                instrutor = Instrutor(nome,email)
                self.instrutores.append(instrutor)
            # Carregar Aulas
            for linha in ficheiroAulas:
                instrutor_nome, horario, numero_max_alunos, duracao = linha.strip().split(',')
                duracao = int(duracao.replace(';', ''))
                
                instrutor = None
                for i in self.instrutores:
                    if i.nome == instrutor_nome:
                        instrutor = i
                        break
                    
                if instrutor:
                    aula = Aula(instrutor, horario, int(numero_max_alunos), int(duracao))
                    self.aulas.append(aula)
                else:
                    print(f"Instrutor {instrutor_nome} não encontrado para a aula às {horario}.")

        except Exception as e:
                print(f"Ocorreu um erro ao carregar os ficheiros: {e}")
 
    def registar_aluno(self, nome, email):
        aluno = Aluno(nome, email)
        self.alunos.append(aluno)
 
        ficheiroAlunos = open("alunos.txt", "a")
        ficheiroAlunos.write(f"{nome},{email};\n")
 
        print(f"\n- Aluno {nome} registado com sucesso -")
        return
 
    def registar_instrutor(self, nome, email):
        instrutor = Instrutor(nome, email)
        self.instrutores.append(instrutor)
 
        ficheiroAlunos = open("instrutores.txt", "a")
        ficheiroAlunos.write(f"{nome},{email};\n")
 
        print(f"\n- Instrutor {nome} registado com sucesso -")
        return
   
    def criar_aula(self, instrutor, horario, numero_max_alunos, duracao):
       
        aula = Aula(instrutor, horario, numero_max_alunos, duracao)
        self.aulas.append(aula)
 
        ficheiroAlunos = open("aulas.txt", "a")
        ficheiroAlunos.write(f"{instrutor.nome},{horario},{numero_max_alunos},{duracao};\n")
 
        clear()
        print(f"\n- Aula criada com instrutor {instrutor.nome} às {horario} (Duração da aula: {duracao} minutos) -")
        return
 
def menu():
    ginasio = Ginasio()
    nomeGinasio = "\n| ginasio Palmadito |\n"
 
    while True:
        print("")
        print("-"*(len(nomeGinasio)-2), end="")
        print(f"{nomeGinasio}")
        print("[1] - Registar Aluno")
        print("[2] - Registar Instrutor")
        print("[3] - Criar Aula")
        print("[4] - Inscrever aluno em aula")
        print("[5] - Mostrar alunos e instrutores registados")
        print("[6] - Mostrar aulas marcadas")
        print("[0] - Sair")
        print("[-1] - Apagar dados (Instantâneo!)")
       
        try:
            escolha = input(">> ")
            clear()
            print("-"*len(nomeGinasio), end="")
        except:
            print("\n- Opção inválida!-")
            continue
 
        if escolha == '-1':
            print("-"*(len(nomeGinasio)-2), end="")
            ficheiroAlunos= open("alunos.txt", "w")
            ficheiroAlunos.close()
            ficheiroInstrutores = open("instrutores.txt", "w")
            ficheiroInstrutores.close()
            ficheiroAulas = open("aulas.txt", "w")
            ficheiroAulas.close()
            clear()
            print("\n- Dados apagados! -")
 
        elif escolha == '1': # Registar um aluno ----------------------------------
            print("\nRegistar Aluno")
            nome = input("Nome do aluno: ")
            email = input("Email do aluno: ")
            ginasio.registar_aluno (nome, email)
 
        elif escolha == '2': # Registar um instrutor ----------------------------------
            print("\nRegistar instrutor")
            nome = input("Nome do instrutor: ")
            email = input("Email do instrutor: ")
            ginasio.registar_instrutor(nome, email)
 
        elif escolha == '3':  # Criar uma aula ----------------------------------
            # Instrutores que não têm aula marcada
            instrutores_disponiveis = [instrutor for instrutor in ginasio.instrutores if instrutor.aula is None]

            if not instrutores_disponiveis:
                print("\n- Não há instrutores disponíveis para criar aulas! -")
                continue

            print("\n- Instrutores disponíveis -")
            for id, instrutor in enumerate(instrutores_disponiveis):
                print(f"{id + 1}. {instrutor.nome}")

            try:
                instrutor_id = int(input("Escolha o número do instrutor: ")) - 1
                instrutor = instrutores_disponiveis[instrutor_id]

                print("\n- Criar aula -")
                # Escolher hora
                while True:
                    horas = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
                            '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
                            '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                            '21:00', '22:00', '23:00']
                    id = 0
                    horasID = []
                    for hora in horas:
                        horasID.append(id)
                        if id % 2 == 0:
                            print(f"{id}. {hora} | ", end="\n")
                        else:
                            print(f"{id}. {hora} | ", end="")
                        id += 1
                    try:
                        escolha = int(input("\nHora da aula (id) : "))
                    except:
                        print("Escolha inválida")

                    if escolha not in horasID:
                        clear()
                        print("- Horário inválido! -\n")
                    else:
                        horario = horas[escolha]
                        print(f"> Horário escolhido: {horario}")
                        break
                numero_max_alunos = int(input("Número máximo de alunos: "))
                duracao = int(input("Duração da aula em minutos: "))
                ginasio.criar_aula(instrutor, horario, numero_max_alunos, duracao)
            except (ValueError, IndexError):
                print("\n- Escolha inválida! -")
                continue
 
        elif escolha == '4': # Inscrever aluno numa aula ----------------------------------
            # Aulas que não estão cheias
            aulas_disponiveis = [aula for aula in ginasio.aulas if len(aula.alunos_inscritos) < aula.numero_max_alunos]
            
            if not ginasio.alunos:
                print("\n- Não há alunos registados! -")
                continue
 
            if not ginasio.aulas:
                print("\n- Não há aulas planeadas! -")
                continue
            
            if not aulas_disponiveis:
                print("\n- Todas as aulas estão lotadas! -")
                continue
 
            print("\n- Alunos registados -")
            for id, aluno in enumerate(ginasio.alunos):
                print(f"{id + 1}. {aluno.nome}")
           
            try:
                aluno_id = int(input("Escolha o número do aluno: ")) - 1
                aluno = ginasio.alunos[aluno_id]
            except (ValueError, IndexError):
                print("Escolha inválida")
                continue
 
            print("\n- Aulas disponíveis -")
            for id, aula in enumerate(aulas_disponiveis):
                print(f"{id + 1}. Aula com {aula.instrutor.nome} às {aula.horario}")
 
            try:
                aula_id = int(input("Escolha o número da aula: ")) - 1
                aula = aulas_disponiveis[aula_id]
                aluno.inscrever_aula(aula)
            except (ValueError, IndexError):
                print("Escolha inválida")
 
        elif escolha == '5': # Mostrar alunos e instrutores registados ----------------------------------
 
            if not ginasio.alunos:
                print("\n- Não há alunos registados! -")
            else:
                print("\n- Alunos Registados -")
                for aluno in ginasio.alunos:
                    print(f"+ Nome: {aluno.nome} | Email: {aluno.email}")
            if not ginasio.instrutores:
                print("\n- Não há instrutores registados! -")
            else:
                print("\n- Instrutores Registados -")
                for instrutor in ginasio.instrutores:
                    print(f"+ Nome: {instrutor.nome} | Email: {instrutor.email}")

        elif escolha == '6': # Mostrar aulas marcadas ----------------------------------
            if not ginasio.aulas:
                print("\n- Não há aulas criadas!-")
            else:
                print("\n- Aulas criadas -")
                for aula in ginasio.aulas:
                    print(f"+ Aula marcada para as {aula.horario} horas com o instrutor {aula.instrutor.nome}")

        elif escolha == '0':
            print("\nAté à próxima!")
            break
 
        else:
            print("Opção inválida. Tente novamente.")
   
    # fim do while
 
menu()