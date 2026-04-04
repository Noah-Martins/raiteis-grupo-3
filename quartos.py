import json

class Quarto():
  dicionario_status = {
    "disponivel" : "Disponível",
    "reservado" : "Reservado",
    "ocupado" : "Ocupado"
  }

  def __init__(self, numero: str, tipo: str, status: str, preco: str):
    self.numero = numero 
    self.tipo = tipo
    self.status = status
    self.preco = float(preco)

  # Exibe os atributos do quarto
  def __str__(self):
    return (f" Numero: {self.numero}\n Tipo: {self.tipo}\n Status: {self.status}\n Preço: R${self.preco}")

  # Muda o atributo staus do quarto
  def mudar_status(self, novo_status: str):
    novo_status = novo_status.strip().lower().replace("í", "i")
    
    if not self.dicionario_status.get(novo_status, None): # Valida o novo_status
      print("Status não existente")

    else:
      self.status = Quarto.dicionario_status[novo_status] # Atualiza o status do quarto

      print("Status atualizado com sucesso!")

class Hotel():
  
  tipos = {
    "standard" : "Standard",
    "master" : "Master",
    "deluxe" : "Deluxe",
    "suite" : "Suite"
  }

  precos = {
    "standard" : "150",
    "master" : "300",
    "deluxe" : "450",
    "suite" : "600"
  }

  def __init__(self):
    self.quartos = self.criar_quartos()
    
  # Preenche o dict quartos do zero
  def criar_quartos(self):
  
    # Cria os quartos Standard do 101 ao 300
    standard = {str(i) : Quarto(str(i), Hotel.tipos["standard"], "Disponivel", Hotel.precos["standard"] ) for i in range(101, 301)}
    # Cria os quartos Master do 301 ao 500
    master = {str(i) : Quarto(str(i), Hotel.tipos["master"], "Disponivel", Hotel.precos["master"]) for i in range(301, 501)}
    # Cria os quartos Deluxe do 501 ao 600
    deluxes = {str(i) : Quarto(str(i), Hotel.tipos["deluxe"], "Disponivel", Hotel.precos["deluxe"])for i in range(501, 601)}
    # Cria os quartos Suite do 601 ao 650
    suites = {str(i) : Quarto(str(i), Hotel.tipos["suite"], "Disponivel", Hotel.precos["suite"]) for i in range(601, 651)}

    return standard | master | deluxes | suites

  # Carrega os dados dos quartos
  def carregar_quartos(self):
    with open("Quartos.json", "r", encoding="utf-8") as arquivo: # Ler o .json com os dados salvos

      self.dados = json.load(arquivo)
      self.quartos = {item['numero']: Quarto(**item) for item in self.dados} # Carrega os dados salvos no dic self.quartos

      return self.quartos
  # Salva os dados dos quartos
  def salvar_quartos(self):
    quartos_formatados = [{chave: valor for chave, valor in q.__dict__.items() if chave != 'dicionario_status'} for q in self.quartos.values()] # Formata os objetos em dicts

    with open("Quartos.json", "w", encoding="utf-8") as arquivo: # Escreve os dados dos quartos no .json
      json.dump(quartos_formatados, arquivo, indent=4, ensure_ascii=False) 

  # Busca um quarto
  def pesquisar_quarto(self, numero_quarto: str):

    return self.quartos.get(numero_quarto, None) # Valida a busca e retonar o objeto quarto






