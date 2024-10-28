#Fazer uma matriz 4x4.
#Imprimir no arquivo TXT.
matriz = []
numeroLinhas = 2
numeroColunas = 2
for linha in range(numeroLinhas):
    inserir = []
    for coluna in range(numeroColunas):
        valor = int(input(f'Digite o valor para a posição[{linha}, {coluna}]'))
        inserir.append(valor)
    matriz.append(inserir)
    
print('Matriz criada')
for imprimir in matriz:
    print(imprimir)
   

                
print("SOMA DOS VALORES DA MATRIZ")
soma = 0
for linha in matriz:
    for valor in linha:
        soma += valor
print("A soma dos VALORES da matriz é: ", soma)
                        
print("Diagonal primaria")
dp = len(matriz)
teste = []
for igualLinhaColuna in range(dp):
    teste.append(matriz[igualLinhaColuna][igualLinhaColuna])
print(teste)
                          
with open('Relatório.txt' , 'w') as arquivo:
    for linha in matriz:
      linha_str = ''.join(map(str,linha))
      arquivo.write(linha_str+'\n')                         
                          
                                                    
                            
                        
                        