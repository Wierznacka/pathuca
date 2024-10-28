matriz = []
numeroLinhas = 2
numeroColunas = 2
for linhas in range(numeroLinhas):
    inserir = []
    for colunas in range(numeroColunas):
        valor = int( input(f' Digite o valor para posição [{linhas} e {colunas}]:'))         
inserir.append(valor)                
matriz.append(inserir)

print("Matriz criada")
for imprimir in matriz:
    print(imprimir)