
def mostrar_menu():
    print("Menu Principal:")
    print("1. para ver valor de fatura. ")
    print("2. para solicitar novo boleto.")
    print("3. falar com o atendente.")
    print("4. Sair")

def processar_escolha(escolha):
    if escolha == '1':
        print("Você escolheu a Opção 1.")
    elif escolha == '2':
        print("Você escolheu a Opção 2.")
    elif escolha == '3':
        print("Você escolheu a Opção 3.")
    elif escolha == '4':
        print("Saindo do programa...")
    else:
        print("Escolha inválida! Tente novamente.")
