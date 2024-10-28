#UPAPEDRO.py

def principal():
    dados_atendimento = []
    while True:
        entrada = str(input("Deseja inserir dados: (Sim/Sair); "))
        if entrada == 'Sair':
            break
principal()
     
        print("***DADOS DO PACIENTE***")
        cpf = int(input("Digite o cpf do paciente: "))
        nome = str(input("Digite o nome do paciente: "))
        data_nascimento_str = int(input("Digite a data_nascimento do paciente: "))

    print("***DADOS ENFERMEIRO***")
    nome_enfermeiro = str(input("Digite o nome do enfermeiro"))
    coren = int(input("Digite o número do coren"))

    print("***DADOS ATENDIMENTO UPA***")
    peso = float(input("Digite o peso do paciente"))
    altura = float(input("Digite a altura do paciente"))
    saturacao = int(input("Digite o SPO2 do paciente"))
    fc = int(input("Digite a frequência cardíaca do paciente"))
    has = str(input("Paciente tem hipertensão arterial"))
    dm = str(input("Paciente tem diabetes Mellitus?"))
    calcular_imc = ()

    imc = calcular_imc(peso, altura)
    atendimento={'paciente': {'cpf': cpf, 'nome': nome, 'data_nascimento': data_nascimento_str}, 
    'enfermeiro': {'nome' : nome_enfermeiro, 'coren' : coren},
    'consulta': {'peso': peso, 'altura': altura, 'saturacao': saturacao, 'fc': fc, 'has': has, 'dm':dm, 'imc':imc}
    } 
    
    dados_atendimento.append(atendimento)
    return dados_atendimento

pessoas = principal()

for atendimento in pessoas:
    print("-" * 20)
    print("Dados do paciente: ")
    print("CPF:", atendimento['paciente'][cpf])
    print("Nome:", atendimento['paciente']['nome'])
    print("COREN:", atendimento['enfermeiro']['coren'])
    print("-" * 20)
    print("Dados da Consulta:")
    print("Peso:", atendimento['consulta']['peso'])
    print("Altura:", atendimento['consulta']['altura'])
    print("Saturacao:", atendimento['consulta']['saturacao'])
    print ("Frequência Cardíaca:", atendimento['consulta']['fc'])
    print("Hipertensão Arterial:", atendimento['consulta']['has'])
    print("Diabetes Mellitus:", atendimento['consulta']['dm'])
    print("IMC:", atendimento['consulta']['imc'])
    
    def calcular_imc(peso,altura):
        imc = peso / (altura ** 2)
        if imc < 18.5:
            classificacao = ("Peso ideal")
            
        elif  19 > imc <= 24.99:
            classificacao = ("Normal")
            
        elif  25 >imc  >= 29.99:
            classificacao = ("Sobrepeso")
            
        elif imc > 30:
            print("O paciente está com obesidade")
        return imc, classificacao 
       
    def calcular_media(peso):
        peso = []
        media = sum(peso) / len(pacientes)
        print(f'A média é: {media}')
        
        pacientes = []
        maior_peso = max(pacientes)
        menor_peso = min(pacientes)
        print(f'O paciente com o maior peso é{maior_peso[0]} com {maior_peso[1]} kg.')
        print(f'O paciente com o menor peso é {menor_peso[0]} com {menor_peso[1]} kg.')
        
        def calcular_media(altura):
            altura = []
            media = sum(altura) / len(pacientes)
            print(f'A média é:{media}')
            calcular_media()
        
        
        
        
    
    





        


