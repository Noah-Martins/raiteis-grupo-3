import csv
import os
from clientes import StatusCliente
from dados import salvar_clientes, salvar_quartos


ARQUIVO_RESERVAS = "reservas.csv"

#persistencia arqv

def salvar_reservas(reservas):
    with open(ARQUIVO_RESERVAS, mode='w', newline='', encoding='utf-8') as file:
        campos = ["id", "cpfcliente", "quarto_id", "diarias", "valor_pagar", "status"]
        writer = csv.DictWriter(file, fieldnames=campos)

        writer.writeheader()
        writer.writerows(reservas)


def carregar_reservas():
    if not os.path.exists(ARQUIVO_RESERVAS):
        return []

    reservas = []

    with open(ARQUIVO_RESERVAS, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            reservas.append({
                "id": int(row["id"]),
                "cpfcliente": row["cpfcliente"],
                "quarto_id": row["quarto_id"],
                "diarias": int(row["diarias"]),
                "valor_pagar": float(row["valor_pagar"]),
                "status": row["status"]
            })

    return reservas

#buscas

def buscar_quarto(quartos, quarto_id):
    return quartos.get(quarto_id)


#registrar reservas 

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
    
    status_limpo = quarto.status.strip().lower().replace("í", "i")
    if status_limpo != "disponivel":
        print("Quarto indisponível.")
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

    salvar_reservas(reservas)
    salvar_clientes(clientesdict)
    salvar_quartos(quartos)

    print(f"Reserva criada. Total: R${valor_pagar:.2f}")

#Consulta

def consultar_reservas(reservas, clientesdict):
    if not reservas:
        print("Sem reservas encontradas.\n")
        return

    print("\n<RESERVAS>\n")

    for r in reservas:
        cliente = clientesdict.get(r["cpfcliente"])
        nome = cliente.nome if cliente else "Desconhecido"

        print(f"""
ID: {r['id']}
Cliente: {nome} ({r['cpfcliente']})
Quarto: {r['quarto_id']}
Diárias: {r['diarias']}
Valor: R${r['valor_pagar']:.2f}
Status: {r['status']}
""")

# Check-in

def realizar_checkin(clientesdict, reservas, quartos):
    cpf = input("CPF do cliente: ").strip()

    cliente = clientesdict.get(cpf)

    if not cliente:
        print("Cliente não registrado\n")
        return
    
    for r in reservas:
        if r["cpfcliente"] == cpf and r["status"] == "reservado":

            quarto = buscar_quarto(quartos, r["quarto_id"])

            if quarto:
                quarto.mudar_status("ocupado")

            r["status"] = "ocupado"
            cliente.status = StatusCliente.HOSPEDADO

            salvar_reservas(reservas)
            salvar_clientes(clientesdict)
            salvar_quartos(quartos)

            print("Check-in realizado.\n")
            return

    print("Reserva não encontrada ou já realizada.\n")

# Check-out

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

            salvar_reservas(reservas)
            salvar_clientes(clientesdict)
            salvar_quartos(quartos)

            print("Check-out realizado.\n")
            return

    print("Reserva não encontrada ou não está em andamento\n")
