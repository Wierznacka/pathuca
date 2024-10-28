#Exercício 2 - lista python.py
#Crie uma lista de 10 números aleatórios entre 1 e 100. Encontre o maior e o menor valor dessa lista.
import random
numeros = [random.randint(1, 100) for _ in range(10)]
maior = max(numeros)
menor = min(numeros)

print("Maior número é: ",maior)
print("Menor número é: ",menor)



