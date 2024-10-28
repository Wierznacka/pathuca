#Exercfuncao2.py
#Faça um programa para atendimento na UPA de Santa Maria, onde o usuario passa pela triagem com a equipe de enfermagem e é solicitado:
# -CPF;
# -Nome;
# -Data de nascimento;
# Onde é verficado: 
# O peso; 
# A altura;
# A saturação;
# frequência cardíaca;
# Se tem hipertensão arterial;
# Se tem diabete Mellitus;
# Após o questionário, o enfermeiro coloca seu nome e seu número do COREN.

# Fazer o cadastro do enfermeiro:

def principal():    
    dados_enfermeiro = []
    while True:
        Nome = int(input("Digite o nome do enfermeiro (ou 0 para sair): "))
        if Nome == 0:
            break        
        COREN = input("Digite o COREN do enfermeiro: ")
        dados_enfermeiro.append([Nome,COREN])
    return dados_enfermeiro

    