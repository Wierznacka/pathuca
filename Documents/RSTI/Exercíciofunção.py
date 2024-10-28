#Foi feita uma pesquisa no SENACRS. 
#Foram coletadosidade e sexo(m/f) dos alunos e nota. 
#Faça um programa que calcule e mostre:
#a) A média das notas dos alunos;
#b) A maior e a menor idade dos alunos;
#c) A quantidade de alunas do SENACRS;
#d) A idade e o sexo do aluno que possui  menor nota;

def calcular_media_notas(alunos):
    notas = [aluno[2] for aluno in alunos]   
    return sum(notas) / len(notas)

def encontrar_aluno_mais_velho(alunos):
    maior_idade = 0
    aluno_mais_velho = None
    for aluno in alunos:
        if aluno[0]>maior_idade:
            maior_idade = aluno[0]
            aluno_mais_velho = aluno
            return aluno_mais_velho
            
def encontrar_aluno_mais_novo(alunos):
        menor_idade = 1000
        aluno_mais_novo = None
        for aluno in alunos:
            if aluno[0]<menor_idade:
                menor_idade = aluno[0]
                aluno_mais_novo = aluno
                return aluno_mais_novo
            
def contar_alunas(alunos):
            cont_alunas = 0
            for aluno in alunos:
                if aluno[1] =='f':
                    cont_alunas += 1
                    return cont_alunas
                
def buscar_aluno_menor_nota(alunos):
    menor_nota = float('inf')
    aluno_menor_nota = 0
    for aluno in alunos:
        if aluno[2]<menor_nota:
            menor_nota = aluno[2]
            aluno_menor_nota = aluno
            return aluno_menor_nota
        
def principal():
    dados_alunos = []
    while True:
        idade = int(input("digite a idade do aluno (ou 0 para sair): "))
        if idade ==0:
            break
        sexo = input("Digite o sexo do aluno (M/F): ")
        nota = float(input("Digite a nota do aluno:"))
        dados_alunos.append([idade, sexo, nota])
        return dados_alunos
    
    alunos = principal()
    media = calcular_media_notas(alunos)
    aluno_mais_velho = encontrar_aluno_mais_velho(alunos)
    aluno_mais_novo = encontrar_aluno_mais_novo(alunos)
    cont_alunas = contar_alunas(alunos)
    aluno_menor_nota = buscar_aluno_menor_nota(alunos)
    
    for aluno in alunos:
        print("-" * 20)
        print('idade.', aluno[0])
        print("Sexo." , aluno[1])
        print("Nota." , aluno[2])
        print("-" * 20)
        
        print("A média das notas dos alunos é: ", media)
        print("O aluno mais velho tem", aluno_mais_velho[0],"anos")
        print("O aluno mais novo tem", aluno_mais_novo[0],"anos")
        print("O número de alunas é:", cont_alunas, "alunas")
        print("-" * 20)
        print("O alluno de menor nota é:",aluno_menor_nota)
              