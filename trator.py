 #criando a classe Trator 
class Trator:
  #Criando o construtor da classe
  def __init__(self, marca, modelo, ano, int, potencia_cv):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.potencia_cv = potencia_cv
    self.andando = False

  # implantação de método de clase3
  def imprimir(self):
    print(f'Marca.........: {self.marca}')
    print(f'Modelo........: {self.modelo}')
    print(f'Ano Fabricação: {self.ano}')
    print(f'Potencia......: {self.potencia_cv}')
    print(f'Em deslocamento: {self.andando}')
    print(f'\n-------------------')

  def andar(self):
    self.__andando = True
    pass
def parar(self):
  self.__andando = False
  pass

def esta_andando(self):
  return self.__andando
  pass
  