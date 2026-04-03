from enum import Enum

class TipoQuarto(Enum):
  """ Tipos de quarto """

  STANDARD = "Standard"
  MASTER = "Master"
  DELUXE = "Deluxe"
  SUITE= "Suite"

class StatusQuarto(Enum):
  """ Status de quarto """

  RESERVADO = "Reservado"
  OCUPADO = "Ocupado"
  DISPONIVEL = "Disponível"

class Quarto:

  def __init__(self, numero: int, tipo: TipoQuarto, valor_diaria: float, status: StatusQuarto = StatusQuarto.DISPONIVEL):
    """ Atributos do quarto """

    self.numero = numero
    self.tipo = tipo
    self.preco = valor_diaria
    self.status = status

  # Exibe as infomações do quarto
  def __str__(self):

    return f" Número: {self.numero}\n Tipo: {self.tipo.value}\n Preço: R${self.preco}\n Status: {self.status.value}"

  # Valida o status recebido
  def validar_status(self, novo_status: str):
    novo_status = novo_status.upper().replace("Í", "I") # Upper() torna a string maiuscula igual o enumerador da StatusQuarto e replace remove o acento

    return StatusQuarto.__members__.get(novo_status) # Retorna status se existir, se não retorna None

  # Muda o status do quarto selecionado
  def mudar_status(self, novo_status: str):
    validacao = self.validar_status(novo_status) # Valida o status antes de mudar (Possivel mudança para validação no codigo principal)

    if validacao is None:
      print("ERRO!.........Status não encontrado")

    else:
      self.status = validacao

      print(f"O quarto {self.numero} agora está {self.status.value}") # Printa o valor do enumerador de StatusQuarto

class Hotel():

  def __init__(self):
    """ Atributos de quarto """

    # criação de um dicionário de precos tabelados
    self.tabela_precos = {
      "Standard" : 100,
      "Master" : 200,
      "Deluxe": 300,
      "Suite" : 500
    }

    self.quartos = self.criar_quartos() # Uni os quartos em um único dict

  # Cria um dict com todos os quartos
  def criar_quartos(self):

    # Cria os quartos Standard do 1 ao 500
    standards = {i : Quarto(i, TipoQuarto.STANDARD, self.tabela_precos["Standard"]) for i in range(1, 501)}
    # Cria os quartos Master do 501 ao 1000
    masters = {i : Quarto(i, TipoQuarto.MASTER, self.tabela_precos["Master"]) for i in range(501, 1001)}
    # Cria os quartos Deluxe do 1001 ao 1250
    deluxes = {i : Quarto(i, TipoQuarto.DELUXE, self.tabela_precos["Deluxe"]) for i in range(1001, 1251)}
    # Cria os quartos Suite do 1251 ao 1351
    suites = {i : Quarto(i, TipoQuarto.SUITE, self.tabela_precos["Suite"]) for i in range(1251, 1351)}

    return standards | masters | deluxes | suites

  # Valida o número de quarto recebido
  def validar_quarto(self, numero_quarto: int):
    return self.quartos.get(numero_quarto) # Retorna quarto se existir, se não retorna None

