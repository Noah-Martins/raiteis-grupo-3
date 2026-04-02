#criar a classe hotel

from enum import Enum

# Definição da classe TipoQuarto
class TipoQuarto(Enum):
  STANDARD = "Standard"
  MASTER = "Master"
  DELUXE = "Deluxe"
  SUITE= "Suite"

# Dicionário de precos
tabela_precos = {
    "Standard" : 100,
    "Master" : 200,
    "Deluxe": 300,
    "Suite" : 500
}

# Definição da classe StatusQuarto
class StatusQuarto(Enum):
  RESERVADO = "Reservado"
  OCUPADO = "Ocupado"
  DISPONIVEL = "Disponível"

# Definição da classe Quarto
class Quarto:
  def __init__(self, numero: int, tipo: TipoQuarto, valor_diaria: float, status: StatusQuarto = StatusQuarto.DISPONIVEL):
    self.numero = numero
    self.tipo = tipo
    self.preco = valor_diaria
    self.status = status

  # Métodos de instância

  # Pesquisa e analise a existência do quarto
  
  # Retorna as infomações do quarto requerido
  def __str__(self):
    return f" Número: {self.numero}\n Tipo: {self.tipo.value}\n Preço: R${self.preco}\n Status: {self.status.value}"
  
  # Muda o status do quarto selecionado
  def mudar_status(self, novo_status: str):

    try: # Testa se o novo_status é um status existente
      novo_status = StatusQuarto(novo_status)
      self.status = novo_status

      print(f"O quarto {self.numero} agora está {self.status.value }")

    except ValueError: # é executado se novo_status não existir em StatusQuarto / valor inadequado
      print(f"{novo_status} não é um status válido")


# Função para definir os quartos
def definir_quartos():
  quartos_standard = {i : Quarto(i, TipoQuarto.STANDARD, tabela_precos["Standard"]) for i in range(1, 501)} # Defini os quartos standart do 1 ao 500, 500 quartos
  quartos_master = {i : Quarto(i, TipoQuarto.MASTER, tabela_precos["Master"]) for i in range(501, 1001)} # Defini os quartos master do 501 ao 1000, 500 quartos
  quartos_deluxe = {i : Quarto(i, TipoQuarto.DELUXE, tabela_precos["Deluxe"])for i in range(1001, 1251)} # Defini os quartos deluxe do 1001 ao 1251, 250 quartos
  quartos_suite = {i : Quarto(i, TipoQuarto.SUITE, tabela_precos["Suite"]) for i in range(1251, 1351)} # Defini os quartos suite do 1251 ao 1350, 100 quartos

  return  quartos_standard |  quartos_master |  quartos_deluxe |  quartos_suite # retorna todos os dicionários em um só dict

# Função para procurar um quarto no dicionário conjunto
def pesquisar_quartos(numero_quarto: int, dicionario_quartos: dict):
  quarto = dicionario_quartos.get(numero_quarto) # procura a chave no dict quartos, se não haver retorna None

  if not quarto: return "Quarto não encontrado" # executando quando quarto = None

  else: return str(quarto) # executado quando a chave do quarto existe, retornado a função __str__

   


# Definição de variáveis importantes
quartos = definir_quartos() # preenche o dict com todos os quartos

