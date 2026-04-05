from clientes import cadastrar_novo_cliente, pesquisar_cliente
from reservas import (
    registrar_reserva,
    consultar_reservas,
    realizar_checkin,
    realizar_checkout
)


SENHA_FUNCIONARIO = "hotelraiteis"

# Menu principal do hotel
def menu_principal():
    print("\n======== MENU PRINCIPAL ========")
    print("1 - Cliente")
    print("2 - Funcionário")
    print("0 - Sair")

    return input("Escolha: ")

# Menu cliente
def menu_cliente(clientes, quartos, reservas):
    while True:
        print("\n--- ÁREA DO CLIENTE ---")
        print("1 - Ver quartos disponíveis")
        print("2 - Fazer reserva")
        print("3 - Buscar meus dados")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            listar_quartos(quartos)

        elif op == "2":
            registrar_reserva(clientes, quartos, reservas)

        elif op == "3":
            cpf = input("CPF: ")
            cliente = pesquisar_cliente(clientes, cpf)
            if cliente:
                print(cliente)
            else:
                print("Cliente não encontrado.")

        elif op == "0":
            break

        else:
            print("Opção inválida.")


# Menu funcionário
def menu_funcionario(clientes, quartos, reservas):
    # a senha é necessária pra acessar essa área
    senha = input("Digite a senha: ") 

    if senha != SENHA_FUNCIONARIO:
        print("Acesso negado.")
        return

    while True:
        print("\n----- ÁREA DO FUNCIONÁRIO -----")
        print("1 - Cadastrar cliente")
        print("2 - Ver quartos")
        print("3 - Consultar reservas")
        print("4 - Check-in")
        print("5 - Check-out")
        print("6 - Cadastrar novo quarto")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_cliente_interface(clientes)

        elif op == "2":
            listar_quartos(quartos)

        elif op == "3":
            consultar_reservas(reservas, clientes)

        elif op == "4":
            realizar_checkin(clientes, reservas, quartos)

        elif op == "5":
            realizar_checkout(clientes, reservas, quartos)
        
        elif op == "6":
            cadastrar_quarto_interface(quartos)

        elif op == "0":
            break

        else:
            print("Opção inválida.")



# Funções auxiliares
def cadastrar_cliente_interface(clientes):
    print("\n----- CADASTRO DE CLIENTE-----")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    
    try:
        idade = int(input("Idade: "))
    except:
        print("Idade inválida.")
        return

    cidade = input("Cidade: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    sucesso, msg = cadastrar_novo_cliente(
        clientes, nome, cpf, idade, cidade, email, telefone
    )

    print(msg)


def cadastrar_quarto_interface(quartos):
    print("\n--- CADASTRAR NOVO QUARTO ---")
    num = input("Número do quarto: ")
    print("Tipos: standard, master, deluxe, suite")
    tipo = input("Tipo: ").lower()
    
    # Importação local para evitar o ImportError
    from quartos import adicionar_novo_quarto
    from dados import salvar_quartos 
    
    if tipo in ["standard", "master", "deluxe", "suite"]:
        if adicionar_novo_quarto(quartos, num, tipo):
            salvar_quartos(quartos)
            print(f"Quarto {num} cadastrado com sucesso!")
    else:
        print("Tipo de quarto inválido.")

def listar_quartos(quartos):
    print("\n----- QUARTOS -----")

    for q in quartos.values():
        print(f"{q.numero} | {q.tipo} | {q.status} | R${q.preco}")