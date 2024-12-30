#Objetivo: 1. pegar o nome dos atletas e seus 5 saltos; 2. Mostrar na tela o nome, saltos e as médias.

#1. pegar o nome dos atletas e seus 5 saltos
def info_dos_atletas():
 info_atleta = dict()
 while  True:

     nome_do_atleta = input('Nome do atleta ou ENTER para sair: ')

     if  not nome_do_atleta.upper():
         break

     saltos = []
     for i in range(1, 6):
         salto = float(input(f'Informe o {i}° salto: '))
         saltos.append(salto)


     media = sum(saltos) / len(saltos)

     info_atleta[nome_do_atleta] = {'Saltos: ': saltos,
                                    'Média: ': media
                                    }
 print('___PONTUAÇÕES DOS ATLETAS___')
 for atleta, info in info_atleta.items():
    print(f'Nome do Atleta: {atleta}')
    print(f'Saltos {info['Saltos: ']}')
    print(f'Media {info['Média: ']}')

if __name__ == '__main__':
   info_dos_atletas()

