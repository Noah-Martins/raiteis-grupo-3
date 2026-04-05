from dados import carregar_clientes, carregar_historico
from quartos import Hotel
from reservas import carregar_reservas
from interface import menu_principal, menu_cliente, menu_funcionario

def main():
    print("="*40)
    print("\t SISTEMA HOTEL RAITEis")
    print("="*40)
    
    # Carregar dados
    clientes = carregar_clientes()
    
    # Instancia o Hotel para garantir a criação dos quartos caso que o CSV não exista ainda
    hotel = Hotel()
    quartos = hotel.quartos 
    
    reservas = carregar_reservas()
    carregar_historico(clientes, reservas)

    # Variável de contole do loop principal
    rodando = True

    while rodando:
        opcao = menu_principal()

        if opcao == "1":
            menu_cliente(clientes, quartos, reservas)

        elif opcao == "2":
            menu_funcionario(clientes, quartos, reservas)

        elif opcao == "0":
            print("\nSalvando dados e encerrando o sistema...")
            rodando = False

        else:
            print("\nOpção inválida. Escolha uma das opções do menu.")

if __name__ == "__main__":
    main()
