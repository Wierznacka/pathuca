#Faça um programa que simule a urna eletrônica. A tela apresentada tem que ser da seguinte forma:
votoAda=0
votoLinus=0
votopatinho=0
while True:
    print("***Candidatos da eleição***")
    print(" 1.candidato Ada Lovelace")
    print(" 2.candidato Linus Tovaldi")
    print(" 3.candidato Patinho Feio")
    print(" 4.Nulo")
    print(" 5.Branco")
    print(" 6.Relatório da Eleição")
    votos = int(input("número de candidato:"))
    if(votos==0):
        print("Sair do Sistema")
        break
    elif(votos==1):
        votoAda+=votos
    elif(votos ==6):
        print("Relatório de eleição:")
        print(f'Candidato Ada Lovelace{votoAda}votos')
        printf'Candidato Linus Tovaldi'{votoLinus} votos')
              
        
    
    