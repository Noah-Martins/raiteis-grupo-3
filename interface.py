# loop principal(contem todo o programa)
while(1):
    print("Escolha uma opção")

    acesso = -1

    # Menu inicial
    while acesso not in [1, 2, 0]:
        print("[1] FUNCIONÁRIO")
        print("[2] CLIENTE")
        print("[0] Sair")
        acesso = int(input())

    # Senha
    if acesso == 1:
        # inicilização da variável
        senha = 0

        while(senha != 1234):
            senha = int(input("SENHA: "))

            if senha != 1234:
                print("SENHA INCORRETA\n")

        # parte do funcionário
        while(1):
            opcao_funcionario = -1

            # menu do funcionário
            while opcao_funcionario not in [1, 2, 0]:
                print("[1] Check-in / Check-out")
                print("[2] Simular Custo")
                print("[0] Sair")

                opcao_funcionario = int(input(""))

            # Check-in / Check-out
            if opcao_funcionario == 1:
                numero_do_quarto = int(input("Numero do quarto: "))
                status = int(input("Novo status ([1]Ocupar [2]Liberar): "))

                if status == 1:
                    print(f"Quarto {numero_do_quarto} agora está OCUPADO")
                else:
                    print(f"Quarto {numero_do_quarto} agora está DISPONí
                    VEL")

            # Preços
            elif opcao_funcionario == 2:
                periodo = int(input("Insira a quantidade de dias: "))

                print("Valor total: ", periodo * 150)
                print("\n")

            # Sair (do menu do funcionário)
            elif opcao_funcionario == 0:
                break

    # parte do cliente
    elif acesso == 2:
        while(1):
            opcao_cliente = -1

            while opcao_cliente not in [1, 2, 0]:
                print("[1] Cadastre-se")
                print("[2] Consultar Preço")
                print("[3] Solicitar Reserva")
                print("[0] Voltar")

                opcao_cliente = int(input(""))

            if opcao_ciente == 1:

            elif opcao_cliente == 2:
                periodo = int(input("Quantos dias pretende ficar? "))
                print("O valor da diaria e 150. Total: ", periodo * )

            elif opcao_cliente == 3:


            elif opcao_cliente == 0:
                break

    # Opção de sair do programa principal
    elif acesso == 0:
        break
