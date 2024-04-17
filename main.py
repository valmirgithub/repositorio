from fazenda import Fazenda
from trator import Trator 




if __name__ =='__main__':
  #criando um trato com o construtor
  trator1 = Trator('John Deere', '9R', 2020, '150','500 cv')
  trator2 = Trator('New Holland', '7630', 2021, '250','120 cv')

#criando uma fazenda com o contrutor vazio 
  faz1 = Fazenda()
#atribuindo os valores indivuialmente
  faz1.nome = 'Fazenda São Jorge'
  faz1.areaHa = 15000
#unica formad e acessar a lista de tratores que é privada
  faz1.add_trator(trator1)
  faz1.add_trator(trator2)
  faz1.listar_tratores()