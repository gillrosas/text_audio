# Classe Bola: Crie uma classe que modele uma bola:
#
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

# class Bola:
#     def __init__(self,cor,circun,material):
#         self.cor = cor
#         self.circun = circun
#         self.material = material
#
#     def MostrarCor(self):
#         print(f'A bola é {self.cor} ')
#
#
#     def trocarCor(self,nova_cor):
#         self.cor = nova_cor
#         print(f'A nova cor do bola: {self.cor}')
# Classe Quadrado: Crie uma classe que modele um quadrado:
#
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
      def __init__(self, tamanho_do_lado):
          self.tamanho_do_lado = tamanho_do_lado
      def info(self,lado):
          lado = self.tamanho_do_lado
          print(f'o lado inicial do quadrado é: {lado}')
      def mudar_de_lado(self,novo_lado):
          self.novo_lado = novo_lado
          print(f'O novo lado da bola vale {self.novo_lado}')
      def calcular_area(self, calc_area):
          calc_area = self.novo_lado ** 2
          print(f'A area do quadrado com novo lado é: {calc_area}')




if __name__ == '__main__':
    # minha_bola = Bola('Azul','3.4',material='Plástico')
    #
    # minha_bola.MostrarCor()
    # minha_bola.trocarCor('Vermelho')
    quadrado = Quadrado(4)
    quadrado.info(quadrado)
    novo_lado = quadrado.mudar_de_lado(6)

    quadrado.calcular_area(novo_lado)



