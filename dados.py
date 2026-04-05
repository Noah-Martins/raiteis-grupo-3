import csv
import os
from clientes import Cliente, popular_base


NOME_ARQUIVO = "clientes.csv"

def salvar_clientes(clientes_dict):
    #Salva o dicionário de clientes no arquivo CSV.
    with open(NOME_ARQUIVO, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['nome', 'cpf', 'idade', 'cidade', 'email', 'telefone', 'status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for cliente in clientes_dict.values():
            writer.writerow(cliente.para_dicionario())

def carregar_clientes():
    #Carrega os clientes do CSV para a memória.
    if not os.path.exists(NOME_ARQUIVO):
        base_inicial = popular_base()
        salvar_clientes(base_inicial) # Salva para criar o ficheiro na primeira vez
        return base_inicial
    
    clientes_carregados = {}
    with open(NOME_ARQUIVO, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            c = Cliente(row['nome'], row['cpf'], int(row['idade']), row['cidade'], row['email'], row['telefone'])
            c.mudar_status(row['status'])
            clientes_carregados[c.cpf] = c
    return clientes_carregados

# Carrega os dados dos quartos
def carregar_quartos():
  from quartos import Quarto
  try:
    with open("Quartos.csv", "r", encoding="utf-8") as arquivo: 
      dados = csv.DictReader(arquivo) # Escreve os dados do CSV em dados
      return  {linha['numero']: Quarto(**linha) for linha in dados} # Retorna os dados do CSV em um dict
  except FileNotFoundError:
      return False

# Salva os dados dos quartos
def salvar_quartos(quartos):
    with open("Quartos.csv", mode='w', newline='', encoding='utf-8') as arquivo:
        colunas = ["numero", "tipo", "status", "preco"]
        writer = csv.DictWriter(arquivo, fieldnames=colunas)
        writer.writeheader()
        for quarto in quartos.values():
            writer.writerow({
                "numero": quarto.numero,
                "tipo":   quarto.tipo,
                "status": quarto.status,
                "preco":  quarto.preco
            })
