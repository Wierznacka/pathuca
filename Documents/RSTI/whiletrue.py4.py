soma = 0
contador = 0
media = 0
maiorValor = 0
menorValor = 999
mediaPares = 0
contaPares = 0
somaPares = 0
contaImpar = 0
while True:
    numero = int(input("Digite o valor: "))
    if(numero < 0):
        print("Sair do sistema")
        break
    elif(numero >0):
        soma+=numero
    contador+=1
    media=soma/contador
    
    if(maiorValor > numero):
        maiorValor = numero
    
    if(menorValor < numero):
        menorValor = numero

    if(numero % 2 == 0):
        contaPares+=1
    somaPares+=numero
    mediaPares = somaPares/contaPares

    if(numero%2==1):
        contaImpar+=1
    porcentagemImpares = (contaImpar*100)/contador
    
print("***RESULTADO***")   
print(f"A soma é {soma}")
print(f"Quantidade de numeros digitados: {contador}")
print(f"A média dos numeros digitados: {media}")
print(f"O maior valor digitado: {media:2f}")
print(f"O menor valor digitado:{menorValor}")
print("f'A média dos números pares:{mediaPares}")
print(f'Prcentagem Impares:{porcentagemImpares}')
