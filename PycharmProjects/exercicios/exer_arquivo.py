def lendo_arquivo():
    with open('usuario.txt', 'r', encoding='utf-8') as arquivo:
        linha = arquivo.readlines()
    return linha

def lista_para_lista_de_dicionario(linha: list):
    lista_de_usuario = []
    lista_modelo = ['Nr','Usuário','Espaço utilizado','% do uso']

    for index, valor in enumerate(linha):
        if index == 0:
            continue
        _valor = valor.split(';')

        dic_usuario = dict()
        for lista_modelo,val in zip(lista_modelo,_valor):
            dic_usuario[lista_modelo] = val
        lista_de_usuario.append(dic_usuario)
    return lista_de_usuario
def mostra_dados(dic_usuario:list):
    print('___INFO USER__')
    for user in dic_usuario:
        print(f'Nr:{user['Nr']} | Usuário: {user['Usuário']}\n ')
        print(f'Espaço Utilizado: {user['Espaço utilizado']}:')







if __name__ == '__main__':
    lin = lendo_arquivo()
    dicionario = lista_para_lista_de_dicionario(linha=lin)
    print(dicionario)
    mostra_dados(dicionario)