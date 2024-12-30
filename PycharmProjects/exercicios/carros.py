def carro_economico():

    carros = ['Gol', 'byd', 'tesla','fiesta','uno']
    consumo = [5,3,6,11,7]
    modelo_mais_economico = consumo[0]
    mais_economico = None
    contador = 1
    carro_consumo = dict()
    for k, v in zip(carros,consumo):
        carro_consumo[k] = v
        if v > modelo_mais_economico:
            modelo_mais_economico = v
            mais_economico = k

    for chave, valor in carro_consumo.items():
        lista_gasto = round((1000 / valor), 2)
        valor_gasto = round(2.25 * lista_gasto, 2)
        print(f'{contador} - {chave} - {valor} - {lista_gasto} litros - R$ {valor_gasto}')
        contador += 1
    print(f"O menor consumo é do {mais_economico}")

if __name__ == '__main__':
    carro_economico()
