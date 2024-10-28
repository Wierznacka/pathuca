#Desenvolver um sistema simples para uma cliníca médica utilizando Python que permita:
#1 - Cadastrar médicos e suas especialidades

medicos = []
pacientes = []
consultas = []
def cadastrar_medico():
    while True:
        nome = str(input("Digite o nome do médico: "))
        crm = str(input("Digite o crm do médico: "))
        especialidade = str(input("Digite a especialidade do médico: "))
        
        medico = {'nome': nome, 'crm' : crm, 'especialidade': especialidade}        
        medicos.append(medico)
        print(f"Cadastro  do médico feito com sucesso!\n")
        
        opcao = input("Deseja cadastrar um novo médico? (sim/não): ").lower()
        if opcao != 'sim':
            break
cadastrar_medico()

def cadastrar_paciente():
    while True:
        nome = input("Digite o nome do paciente: ")
        data_nascimento_str = input("Digite a data nascimento: ")
        paciente = {'nome' : nome, 'data nascimento' : data_nascimento_str}
        paciente.append(paciente)
        print(f'Cadastro  do paciente feito com sucesso!\n')
        
        opcao = input("Deseja cadastrar um novo paciente? (sim/não): ").lower()
        if opcao != "sim":
            break
cadastrar_paciente()  
      
def agendar_consulta():
    while True:
        paciente = str(input("Digite o nome do paciente: "))
        medico = str(input("Digite o nome do médico desejado: "))
        data = input("Digite a data escolhida: ")
        descricao = str(input("Digite os sintomas do paciente: "))
        consultas.append(consultas)
        print(f'Sua consulta foi agendada com sucesso!\n')

        opcao = input("Deseja agendar uma nova consulta? (sim/não): ").lower
        if opcao != 'sim':
                break
agendar_consulta()


dados_cadastro = principal()


    
        
     