#Exercicio cores 
cores = []
numeroCores = 3
for i in range(numeroCores):
    nome = input("Digite as cores: ")
    cores.append(nome)
print(cores)
for cor in cores:
        nome= input("Digite a cor a remover: ")
        cores.remove(nome)
        break
print(cores)