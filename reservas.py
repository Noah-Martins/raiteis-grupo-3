from dados import clientes, quartos, reservas
from clientes import StatusCliente

#BUSCAS#

def buscar_quarto(quartos, quarto_id):
    for i in quartos:
        if i["id"] == quarto_id:
            return i
    return None


def buscar_reservas(reservas, reserva_id):
    for j in reservas:
        if j["id"] == reserva_id:
            return j
    return j

#REGISTRAR RESESERVAS#

def registrar_reserva(clientesdict, quartos, reservas):
    cpf = input("CPF do cliente: ").strip()

    cliente = clientesdict.get(cpf)

    if not cliente:
        print("Cliente não registrado.\n")
        return
    
    try:
        quarto_id = int(input("Número do quarto: "))
        diarias = int(input("Quantidade de diárias: "))

    except:
        print("Entrada não-válida.\n")
        return
    
    if diarias <= 0:
        print("É preciso de no mínimo uma diária.\n")
        return
    
    quarto = buscar_quarto(quartos, quarto_id)

    if not quarto:
        print("Quarto não registrado. \n")
        return
    
    if quarto["status"] != "disponivel":
        print("Quarto indisponìvel.\n")
        return
    
    valor_pagar = quarto["preco"]*diarias

    reserva = {
        "id": len(reservas) + 1,
        "cpfcliente": cpf,
        "quarto_id": quarto_id,
        "diarias": diarias,
        "valor_pagar": valor_pagar,
        "status": "reservado"
    }

    reservas.append(reserva)

    quarto["status"] = "reservado"
    cliente.status = StatusCliente.RESERVADO
    cliente.historico.append(reserva)
    print("Reserva criada! Total: R${valor_pagar}")


def consultar_reservas(reservas, clientesdict):
    if not reservas("Sem reservas encontradas.\n")
    return

    print("\n <RESERVAS>\n")

    for i in reservas:
        cliente = clientesdict.get(r["cpfcliente"])

        nomecliente = cliente.nome

         print(f"""
ID: {r['id']}
Cliente: {nome_cliente} ({r['cpfcliente']})
Quarto: {r['quarto_id']}
Diárias: {r['diarias']}
Valor: R${r['valor_pagar']:.2f}
Status: {r['status']}
""")
