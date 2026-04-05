import csv
class Configuracoes():
   dicionario_status = { "disponivel" : "Disponível", "reservado" : "Reservado", "ocupado" : "Ocupado"}
   tipos = {"standard" : "Standard", "master" : "Master", "deluxe" : "Deluxe", "suite" : "Suite"}
   precos = {"standard" : "150", "master" : "300", "deluxe" : "450", "suite" : "600"} 
   # Inverter dicionários para salvar as chaves no CSV
   status_invertido = {valor: chave for chave, valor in dicionario_status.items()}
   tipos_invertido = {valor: chave for chave, valor in tipos.items()}
   precos_invertido = {valor: chave for chave, valor in precos.items()}

class Quarto():

  def __init__(self, numero: str, tipo: str, status: str, preco: str):
    self.numero = numero 
    self.tipo = Configuracoes.tipos[tipo]
    self.status = Configuracoes.dicionario_status[status]
    self.preco = float(Configuracoes.precos[preco])

  # Exibe os atributos do quarto
  def __str__(self):
    return (f" Numero: {self.numero}\n Tipo: {self.tipo}\n Status: {self.status}\n Preço: R${self.preco}")

  # Muda o atributo status do quarto
  def mudar_status(self, novo_status: str):
    novo_status = novo_status.strip().lower().replace("í", "i") # Formata novo_status no formato das chaves de configuracoes.dicionario_status
    
    if not Configuracoes.dicionario_status.get(novo_status, None): # Valida o novo_status
      print("Status não existente")
    else:
      self.status = Configuracoes.dicionario_status[novo_status] # Atualiza o status do quarto
      
      print("Status atualizado com sucesso!")

class Hotel():
  def __init__(self):
    from dados import carregar_quartos
    
    self.quartos = carregar_quartos()
    
  # Preenche o dict quartos do zero
  def criar_quartos(self):
  
    # Cria os quartos Standard do 101 ao 300
    standard = {str(i) : Quarto(str(i), "standard", "disponivel", "standard") for i in range(101, 301)}
    # Cria os quartos Master do 301 ao 500
    master = {str(i) : Quarto(str(i), "master", "disponivel","master") for i in range(301, 501)}
    # Cria os quartos Deluxe do 501 ao 600
    deluxes = {str(i) : Quarto(str(i), "deluxe", "disponivel","deluxe")for i in range(501, 601)}
    # Cria os quartos Suite do 601 ao 650
    suites = {str(i) : Quarto(str(i), "suite", "disponivel", "suite") for i in range(601, 651)}

    return standard | master | deluxes | suites 
    
  # Busca um quarto
  def pesquisar_quarto(self, numero_quarto: str):

    return self.quartos.get(numero_quarto, None) # Valida a busca e retonar o objeto quarto





