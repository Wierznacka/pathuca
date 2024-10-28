#Exercicio Matriz 1.py
#leia uma matriz de 5x5 elementos. 
#Imprima a matriz com os valores

matriz = []
numeroLinhas = 5
numeroColunas = 5
for linhas in range(numeroLinhas):
    inserir = []
    for colunas in range(numeroColunas):
        valor = int( input(f' Digite o valor para posição [{linhas} e {colunas}]:'))         
        inserir.append(valor)                
matriz.append(inserir)

print("Matriz criada")
for imprimir in matriz:
    print(imprimir)
    
    
    
print("DIAGONAL PRIMARIA")
dp = len(matriz)
teste = []
for igualLinhaColuna in range(dp):
    teste.append(matriz[igualLinhaColuna][igualLinhaColuna])
    print(teste)
diagonalPrimaria = len(matriz)
for dp in range(diagonalPrimaria):
          print(matriz[dp][dp])            

print("DIAGONAL SECUNDARIA")
diagonalSecundaria = len(matriz)
for ds in range(diagonalSecundaria):
    print(matriz[diagonalSecundaria-ds-1][ds])
    
    print("Matriz valor MAIOR que 10: ")
    for valor in matriz:
        if valor > 10:
            print(valor)
            
            print("Matriz MENOR valor")
            menor = len(matriz)
            for linha in range(menor):
                if matriz[linha][colunas] < menor:
                    menor = matriz[linha][colunas]
                    print(menor)
                    
        with open('Relatório.txt', 'w') as arquivo:
            for linha in matriz:
                linha_str = ''.join(map(str,linha))
                
                arquivo.write(linha_str +'\n')
                arquivo.write(f'A soma dos elementos da matriz é: {soma}')
                arquivo.write(f'O menor valor da matriz é: {menor}\n')
                arquivo.write(f'A diqagonal secundária da matriz é: {ds}\n')
                arquivo.write(f'A diagonal principal da matriz é: {dp}\n')
                print("Relatório salvo!!!")