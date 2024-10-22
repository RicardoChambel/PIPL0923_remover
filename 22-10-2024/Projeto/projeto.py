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

        print(f"\n- Aula criada com instrutor {instrutor.nome} às {horario}. -")
        return

def menu():
    ginásio = Ginasio()

    while True:
        print("\n\tGinásio Palmadito")
        print("[1] - Registar Aluno")
        print("[2] - Registar Instrutor")
        print("[3] - Criar Aula")
        print("[4] - Inscrever aluno em aula")
        print("[5] - Mostrar alunos e instrutores registados")
        print("[0] - Sair")
        
        try:
            escolha = input(">> ")
            clear()
        except:
            print("\n- Opção inválida!-")
            continue

        if escolha == '1':
            print("\nRegistar Aluno")
            nome = input("Nome do aluno: ")
            email = input("Email do aluno: ")
            ginásio.registar_aluno (nome, email)

        elif escolha == '2':
            print("\nRegistar instrutor")
            nome = input("Nome do instrutor: ")
            email = input("Email do instrutor: ")
            ginásio.registar_instrutor(nome, email)

        elif escolha == '3':
            if not ginásio.instrutores:
                print("\n- Não há instrutores registados! -")
                continue

            print("- Instrutores disponíveis -")
            for id, instrutor in enumerate(ginásio.instrutores):
                print(f"{id + 1}. {instrutor.nome}")

            try:
                instrutor_id = int(input("Escolha o número do instrutor: ")) - 1
                instrutor = ginásio.instrutores[instrutor_id]
                if instrutor.aula is not None:
                    print("\n- O instrutor já tem aula marcada! -")
                    continue

                print("\n- Criar aula -")
                horario = input("Horário da aula (ex: 10:00): ")
                numero_max_alunos = int(input("Número máximo de alunos: "))
                duracao = int(input("Duração da aula (minutos): "))
                ginásio.criar_aula(instrutor, horario, numero_max_alunos, duracao)
            except (ValueError, IndexError):
                print("\n- Escolha inválida! -")
                continue

        elif escolha == '4':
            if not ginásio.alunos:
                print("\n- Não há alunos registados! -")
                continue

            print("\n- Alunos registados -")
            for id, aluno in enumerate(ginásio.alunos):
                print(f"{id + 1}. {aluno.nome}")
            
            try:
                aluno_id = int(input("Escolha o número do aluno: ")) - 1
                aluno = ginásio.alunos[aluno_id]
            except (ValueError, IndexError):
                print("Escolha inválida")
                continue

            if not ginásio.aulas:
                print("\n- Não há aulas planeadas! -")
                continue

            print("\n- Aulas disponíveis -")
            for id, aula in enumerate(ginásio.aulas):
                print(f"{id + 1}. {aula.instrutor.nome} às {aula.horario}")

            try:
                aula_id = int(input("Escolha o número da aula: ")) - 1
                aula = ginásio.aulas[aula_id]
                aluno.inscrever_aula(aula)
            except (ValueError, IndexError):
                print("Escolha inválida")
                continue

        elif escolha == '5':
            print("\n- Alunos Registados -")
            for aluno in ginásio.alunos:
                print(f"Nome: {aluno.nome}, Email: {aluno.email}")
        
            print("\n- Instrutores Registados -")
            for instrutor in ginásio.instrutores:
                print(f"Nome: {instrutor.nome}, Email: {instrutor.email}")

        elif escolha == '0':
            print("Ate a proxima!")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()  # Iniciar o programa