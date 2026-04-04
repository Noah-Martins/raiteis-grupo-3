import json 

class Quarto():
  def __init__(self, numero: str, tipo: str, status: str, preco: str):
    self.numero = numero
    self.tipo = tipo
    self.status = status
    self.preco = float(preco)
    
    self.dicionario_status = {
      "disponivel" : "Disponível",
      "reservado" : "Reservado",
      "ocupado" : "Ocupado"
    }
  
  # Exibe os atributos do quarto
  def __str__(self):
    return (f" Numero: {self.numero}\n Tipo: {self.tipo}\n Status: {self.status}\n Preço: R${self.preco}")
  
  # Muda o atributo staus do quarto
  def mudar_status(self, novo_status: str):
    novo_status = self.dicionario_status.get(novo_status, None) # Valida o novo_status 

    if not novo_status:
      print("Status não existente")
      
    else:
      self.status = novo_status

      print("Status atualizado com sucesso!")  

class Hotel():
  def __init__(self):
    self.quartos = {}

    self.tipos = {
      "standard" : "Standard",
      "master" : "Master",
      "deluxe" : "Deluxe",
      "suite" : "Suite"
    }

    self.precos = {
      "standard" : "150",
      "master" : "300",
      "deluxe" : "450",
      "suite" : "600"
    }
  
  # Carrega os dados dos quartos
  def carregar_quartos(self):
    with open("Quartos.json", "r", encoding="utf-8") as arquivo:

      self.dicionario = json.load(arquivo)
      self.quartos = {item['numero']: Quarto(**item) for item in self.dicionario}

      return self.quartos
  # Salva os dados dos quartos
  def salvar_quartos(self):
    quartos_formatados = [{chave: valor for chave, valor in q.__dict__.items() if chave != 'dicionario_status'} for q in self.quartos.values()]


    with open("Quartos.json", "w", encoding="utf-8") as arquivo:
      json.dump(quartos_formatados, arquivo, indent=4, ensure_ascii=False)
  
  # Busca um quarto 
  def pesquisar_quarto(self, numero_quarto: str):
    
    return self.quartos.get(numero_quarto, None) # Valida a busca

    
  
raiteis = Hotel()

raiteis.carregar_quartos()



(raiteis.pesquisar_quarto("101")).mudar_status("disponivel")



raiteis.salvar_quartos()


