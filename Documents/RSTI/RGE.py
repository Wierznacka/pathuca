from corsan import mostrar_menu, processar_escolha
def main():
    escolha = ''
    while escolha != '4':  # Enquanto o usuário não escolher sair
        mostrar_menu()
        escolha = input("Digite o número da sua escolha: ")
        processar_escolha(escolha)

if __name__ == "__main__":
    main()