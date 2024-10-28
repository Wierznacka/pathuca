#Exemplo exercicio DEF
def somar_dois_numeros(a,b):
    resultado = a + b
    return resultado

def multiplicar_soma_triplo(soma):
    resultado = soma * 3
    return resultado

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

soma = somar_dois_numeros(a,b)
multiplicar = multiplicar_soma_triplo(soma)

print("Soma:", soma)
print("multiplicar:", multiplicar)

    