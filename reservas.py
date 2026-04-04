from dados import clientes, quartos, reservas
from clientes import StatusCliente

# BUSCAS

def buscar_quarto(quartos, quarto_id):
    return quartos.get(quarto_id)


def buscar_reservas(reservas, reserva_id):
    for r in reservas:
        if r["id"] == reserva_id:
            return r
    return None

# REGISTRAR RESERVA


def registrar_reserva(clientesdict, quartos, reservas):
    cpf = input("CPF do cliente: ").strip()

    cliente = clientesdict.get(cpf)

    if not cliente:
        print("Cliente não registrado.\n")
        return
    
    try:
        quarto_id = input("Número do quarto: ").strip()
        diarias = int(input("Quantidade de diárias: "))
    except:
        print("Entrada não-válida.\n")
        return
    
    if diarias <= 0:
        print("É preciso de no mínimo uma diária.\n")
        return
    
    quarto = buscar_quarto(quartos, quarto_id)

    if not quarto:
        print("Quarto não registrado.\n")
        return
    
    if quarto.status != "Disponível":
        print("Quarto indisponível.\n")
        return
    
    valor_pagar = quarto.preco * diarias

    reserva = {
        "id": len(reservas) + 1,
        "cpfcliente": cpf,
        "quarto_id": quarto_id,
        "diarias": diarias,
        "valor_pagar": valor_pagar,
        "status": "reservado"
    }

    reservas.append(reserva)

    quarto.mudar_status("reservado")
    cliente.status = StatusCliente.RESERVADO
    cliente.historico_reservas.append(reserva)

    print(f"Reserva criada. Total: R${valor_pagar:.2f}")

# CONSULTAR RESERVAS

def consultar_reservas(reservas, clientesdict):
    if not reservas:
        print("Sem reservas encontradas.\n")
        return

    print("\n<RESERVAS>\n")

    for r in reservas:
        cliente = clientesdict.get(r["cpfcliente"])

        nomecliente = cliente.nome if cliente else "Desconhecido"

        print(f"""
ID: {r['id']}
Cliente: {nomecliente} ({r['cpfcliente']})
Quarto: {r['quarto_id']}
Diárias: {r['diarias']}
Valor: R${r['valor_pagar']:.2f}
Status: {r['status']}
""")

# CHECK-IN

def realizar_checkin(clientesdict, reservas, quartos):
    cpf = input("CPF do cliente: ").strip()

    cliente = clientesdict.get(cpf)

    if not cliente:
        print("Cliente não registrado.\n")
        return
    
    for r in reservas:
        if r["cpfcliente"] == cpf and r["status"] == "reservado":

            quarto = buscar_quarto(quartos, r["quarto_id"])

            if quarto:
                quarto.mudar_status("ocupado")

            r["status"] = "ocupado"
            cliente.status = StatusCliente.HOSPEDADO

            print("Check-in realizado.\n")
            return

    print("Reserva não encontrada ou já realizada.\n")

# CHECK-OUT

def realizar_checkout(clientesdict, reservas, quartos):
    cpf = input("CPF do cliente: ").strip()

    cliente = clientesdict.get(cpf)

    if not cliente:
        print("Cliente não registrado.\n")
        return

    for r in reservas:
        if r["cpfcliente"] == cpf and r["status"] == "ocupado":

            quarto = buscar_quarto(quartos, r["quarto_id"])

            if quarto:
                quarto.mudar_status("disponivel")

            r["status"] = "finalizado"
            cliente.status = StatusCliente.INATIVO

            print("Check-out realizado.\n")
            return

    print("Reserva não encontrada ou não está em andamento.\n")

