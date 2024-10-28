#PG - aula 1
#Calcular o IMC de um grupo de pessoas.

def calcular_imc(peso,altura):
        imc = peso / (altura ** 2)
        if imc < 18.5: 
           classificacao = "Peso ideal"
            
        elif   19 > imc <= 24.99:
            classificacao = "Normal"
            
        elif   25 > imc >= 29.99:
            classificacao = "Sobrepeso"
            
        elif imc > 30:
            classificacao = "Obesidade"
        return imc, classificacao
        
lista1 = []
nome = str(input("Digite seu nome: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = calcular_imc(peso, altura)
print(imc)
lista1.append({'nome': nome, 'altura': altura, 'peso': peso, 'imc': imc[1]})
print(lista1)

