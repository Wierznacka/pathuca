#Exercício 8 - LISTA PYTHON
#Crie uma lista com 10 números aleatórios. Remova todos os números pares da lista.
numeros = [1,2,3,4,5,6,7,8,9,10]
for valor in numeros:
    if valor%2==0:
        numeros.remove(valor)
        print(numeros)  