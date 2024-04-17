class Talhao:
  def __init__(self,talhao_id,talhao_ha):
    self.talhao_id = talhao_id
    self.talhao_ha = talhao_ha

  def print (self):
    print(f'\n-------------------)
    print(f"Identificação do taulhao: {self.talhao_id}")
    print(f"Área do talhao: {self.talhao_ha}")