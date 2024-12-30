carros = ['Gol','BYD', 'Tesla','Fiesta','Fusca']
consumo = [10,5,3,11,12]

lista_de_carro = []
info_carros = dict()
litro = []
gasto = []
for i in consumo:
    litros = (1000/i)
    litro.append(litros)
    gastos = litros*2.25
    gasto.append(gastos)
    # print(litro)

for carro,valor,valor1,gas in zip(carros,consumo,litro,gasto):
    info_carros[carro] = {'Consumo': valor,
                          'Km consumidos ':valor1,
                          'Gastos': gas}
lista_de_carro.append(info_carros)
print(lista_de_carro)



for carro, info in info_carros.items():
    consumo = info[('Consumo')]
    print(f'{carro}: {consumo}')









