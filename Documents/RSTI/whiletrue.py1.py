while True:
    print(" *** CALCULADORA ***")
    print("1.Adição")
    print("2.subtração")
    print("3.multiplicação")
    print("4.divisão")
    print("0. sair")
    opção = int(input("escolha a opção:"))
    if(opção == 0):
        print("Sair do Sistema!!!")
        break
    valor1 = int(input("Digite valor 1: "))
    valor2 = int(input("Digite o valor 2: "))
    if(opção==1):
        resultado = valor1+valor2
        print("Resultado: ",resultado)
    elif(opção==2):
        resultado = valor1-valor2
        print("Resultado: ",resultado)
    if(opção==3):
        resultado = valor1*valor2
        print("Resultado: ",resultado)
    elif(opção==4):
        resultado = valor1/valor2
        print("Resultado: ",resultado)
        if(valor2 == 0):
            print("Divisão não é permitida!!!")
        else:
            resultado = valor1/valor2
            print("Resultado: ",resultado)
    else:
       print("Operação não permitida!!!")
    