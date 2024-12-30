


def ler_arquivo_vendas(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8")as arquivo:
        linha = arquivo.readlines()
    return linha

def calcular_total_de_vendas(arquivo_vendas:list):
    list_iten = []
    total_vendas = dict()
    list_label = ['Produto','Quantidade','Preço']
    for index, valor in enumerate(arquivo_vendas):
        if index == 0:
            continue
        _valor = valor.split(',')
        dict_item = dict()
        for label,v in zip(list_label,_valor):
            dict_item[label] = v.strip()
        list_iten.append(dict_item)
    print(list_iten)
    quantidade_camiseta = []
    preco_camiseta = []
    quantidade_calc = []
    preco_calca = []
    quantidade_tenis = []
    preco_tenis = []
    for item in list_iten:
        if item.get('Produto') == 'Camiseta':
            quantidade_camiseta.append(item.get('Quantidade'))
            preco_camiseta.append(item.get('Preço'))
        if item.get('Produto') == 'Calça':
            quantidade_calc.append(item.get('Quantidade'))
            preco_calca.append(item.get('Preço'))
        if item.get('Produto') == 'Tênis':
            quantidade_tenis.append(item.get('Quantidade'))
            preco_tenis.append(item.get('Preço'))

    # print(f'Quantidade: {quantidade_camiseta}')
    # print(f' Preço: {preco_camiseta}')
    # print(f'Quantidade: {quantidade_calc}')
    # print(f' Preço: {preco_calca}')
    # print(f'Quantidade: {quantidade_tenis}')
    # print(f' Preço: {preco_tenis}')

    preco_total_camisetas = []
    preco_total_calca = []
    preco_total_tenis = []
    total_camiseta = 0
    total_calca = 0
    total_tenis = 0
    for i in range(11):
        preco_total_camisetas.append(float(quantidade_camiseta[i]) * float(preco_camiseta[i]))
        preco_total_calca.append(float(quantidade_calc[i]) * float(preco_calca[i]))
        total_camiseta += preco_total_camisetas[i]
        total_calca += preco_total_calca[i]
    # print(preco_total_camisetas)
    for i in range(7):
        preco_total_tenis.append(float(quantidade_tenis[i]) * float(preco_tenis [i]))
        total_tenis += preco_total_tenis [i]
    # print(f'Preço total das Camisetas:{total_camiseta} ')
    # print(f'Preço totall das calças: {total_calca}')
    total_vendas['Camiseta'] = total_camiseta
    total_vendas['Calça'] = total_calca
    total_vendas['Tênis'] = total_tenis
    return total_vendas
def gerar_relatorio(total_vendas= dict()):
    print('__Relatório de Vendas__')
    for elem in total_vendas:
        print(f'{elem}: {total_vendas[elem]}')
    pass

def executar():
    vendas = ler_arquivo_vendas(nome_arquivo='arquivo_vendas.txt')
    totais = calcular_total_de_vendas(arquivo_vendas=vendas)
    gerar_relatorio(total_vendas=totais)


if __name__ == '__main__':
    executar()


