from enum import Enum

# Definição do status do cliente
class StatusCliente(Enum):
    ATIVO      = "Ativo"       # cadastrado mas sem reserva
    RESERVADO  = "Reservado"   # tem reserva mas ainda não chegou
    HOSPEDADO  = "Hospedado"   # fez check-in
    INATIVO    = "Inativo"     # fez check-out

# Definição da classe Cliente
class Cliente:
    def __init__(self, nome: str, cpf: str, idade: int, cidade: str, email: str, telefone: str):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.cidade = cidade
        self.email = email
        self.telefone = telefone
        self.status = StatusCliente.ATIVO
        self.historico_reservas = []
