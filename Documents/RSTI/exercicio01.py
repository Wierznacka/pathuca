n1= int(input("Digite o primeiro valor: "))
n2= int(input("Digite o segundo valor: "))
contador=0
for numero in range(n1, n2+1):
    if(numero%2 != 0):
        contador+=1
        print (numero)
        print (contador)

