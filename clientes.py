from enum import Enum
import os
from dados import salvar_clientes

# Definição do status do cliente
class StatusCliente(Enum):
    ATIVO      = "Ativo"       # cadastrado mas sem reserva
    RESERVADO  = "Reservado"   # tem reserva mas ainda não chegou
    HOSPEDADO  = "Hospedado"   # fez check-in
    INATIVO    = "Inativo"     # fez check-out

# Definição da classe Cliente
class Cliente:
    def __init__(self, nome: str, cpf: str, idade: int, cidade: str, email: str, telefone: str):

            # Validação de campos vazios 
        if not nome.strip() or not cpf.strip() or not email.strip():
            raise ValueError("Erro: Nome, CPF e Email são obrigatórios e não podem ser vazios.")
        
        # Validação de tipo e valor de idade 
        if not isinstance(idade, int) or idade <= 0:
            raise ValueError("Erro: A idade deve ser um número inteiro positivo.")

        # Validação básica de email
        if "@" not in email:
            raise ValueError("Erro: O email inserido é inválido.")
        
            self.nome = nome
            self.cpf = cpf
            self.idade = idade
            self.cidade = cidade
            self.email = email
            self.telefone = telefone
            self.status = StatusCliente.ATIVO
            self.historico_reservas = []

    def __str__(self):
        return f"{self.nome} ({self.cpf}) - Status: {self.status.value}"
    

    def para_dicionario(self):
        return {
            'nome': self.nome,
            'cpf': self.cpf,
            'idade': self.idade,
            'cidade': self.cidade,
            'email': self.email,
            'telefone': self.telefone,
            'status': self.status.value
        }

def cadastrar_novo_cliente(clientes_dict, nome, cpf, idade, cidade, email, telefone):
    # Verifica duplicidade (CPF é a chave única) [cite: 36]
    if cpf in clientes_dict:
        return False, "Erro: Este CPF já está cadastrado."

    try:
        # Tenta criar o objeto (isso vai disparar as validações do __init__)
        novo = Cliente(nome, cpf, idade, cidade, email, telefone)
        clientes_dict[cpf] = novo
        
       # Salva a nova base de clientes no arquivo CSV
        salvar_clientes(clientes_dict)
        return True, f"Cliente {nome} cadastrado com sucesso!"
    except ValueError as x:
        return False, str(x)


def pesquisar_cliente(clientes_dict, cpf):
    return clientes_dict.get(cpf, None)




# Função para popular a base com 20 clientes fictícios
def popular_base():

    base = [

        ("João Silva",       "111.111.111-11", 34, "Fortaleza",      "joao@email.com",    "(85) 99999-0001"),

        ("Maria Souza",      "222.222.222-22", 28, "Recife",         "maria@email.com",   "(81) 99999-0002"),

        ("Carlos Oliveira",  "333.333.333-33", 45, "Salvador",       "carlos@email.com",  "(71) 99999-0003"),

        ("Ana Lima",         "444.444.444-44", 22, "Natal",          "ana@email.com",     "(84) 99999-0004"),

        ("Pedro Costa",      "555.555.555-55", 31, "Maceió",         "pedro@email.com",   "(82) 99999-0005"),

        ("Juliana Martins",  "666.666.666-66", 27, "São Luís",       "ju@email.com",      "(98) 99999-0006"),

        ("Rafael Pereira",   "777.777.777-77", 38, "Teresina",       "rafa@email.com",    "(86) 99999-0007"),

        ("Fernanda Rocha",   "888.888.888-88", 24, "Fortaleza",      "fe@email.com",      "(85) 99999-0008"),

        ("Lucas Alves",      "999.999.999-99", 19, "Mossoró",        "lucas@email.com",   "(84) 99999-0009"),

        ("Beatriz Nunes",    "100.010.010-10", 33, "Campina Grande", "bia@email.com",     "(83) 99999-0010"),

        ("Thiago Ferreira",  "110.011.001-10", 41, "Aracaju",        "thiago@email.com",  "(79) 99999-0011"),

        ("Camila Dias",      "120.012.001-20", 26, "Fortaleza",      "camila@email.com",  "(85) 99999-0012"),

        ("Gustavo Carvalho", "130.013.001-30", 52, "João Pessoa",    "gus@email.com",     "(83) 99999-0013"),

        ("Larissa Moura",    "140.014.001-40", 29, "Recife",         "lari@email.com",    "(81) 99999-0014"),

        ("Bruno Teixeira",   "150.015.001-50", 36, "Natal",          "bruno@email.com",   "(84) 99999-0015"),

        ("Patrícia Gomes",   "160.016.001-60", 23, "São Luís",       "pat@email.com",     "(98) 99999-0016"),

        ("Diego Nascimento", "170.017.001-70", 44, "Salvador",       "diego@email.com",   "(71) 99999-0017"),

        ("Vanessa Castro",   "180.018.001-80", 30, "Teresina",       "vane@email.com",    "(86) 99999-0018"),

        ("Rodrigo Barbosa",  "190.019.001-90", 37, "Maceió",         "rod@email.com",     "(82) 99999-0019"),

        ("Isabela Mendes",   "200.020.002-00", 21, "Fortaleza",      "isa@email.com",     "(85) 99999-0020"),

    ]

    return {cpf: Cliente(nome, cpf, idade, cidade, email, tel)

            for nome, cpf, idade, cidade, email, tel in base} 