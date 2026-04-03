from enum import Enum

""" Classe TipoQuarto"""

# Definição da classe TipoQuarto
class TipoQuarto(Enum):
  STANDARD = "Standard"
  MASTER = "Master"
  DELUXE = "Deluxe"
  SUITE= "Suite"

""" Classe StatusQuarto"""

# Definição da classe StatusQuarto
class StatusQuarto(Enum):
  RESERVADO = "Reservado"
  OCUPADO = "Ocupado"
  DISPONIVEL = "Disponível"

""" Classe Quarto """

# Definição da classe Quarto
class Quarto:
  def __init__(self, numero: int, tipo: TipoQuarto, valor_diaria: float, status: StatusQuarto = StatusQuarto.DISPONIVEL):
    self.numero = numero
    self.tipo = tipo
    self.preco = valor_diaria
    self.status = status
  # Exibe as infomações do quarto requerido
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

""" Classe Hotel """

# Defini a classe hotel que abrangem as demais classes ligadas aos quartos
class Hotel():
  def __init__(self):
    """ Dicionário de preços """
     
    # criação de um dicionário de precos tabelados
    self.tabela_precos = {
      "Standard" : 100,
      "Master" : 200,
      "Deluxe": 300,
      "Suite" : 500
    }

    self.quartos = self.criar_quartos()
 
  # Função de criação de quartos
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

  # Função de busca/validação de quartos
  def buscar_quarto(self, numero_quarto: int):
    quarto = self.quartos.get(numero_quarto)

    if quarto:
      return quarto
    else: 
      print("ERRO!.........Quarto não encontrado")
  
hotel = Hotel()  
