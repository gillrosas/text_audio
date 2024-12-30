def manipulandoarquivo():

     #1. abrir o arquivo, ler as linhas do arquivo
       with open('usuario.txt','r', encoding = 'utf-8') as arquivo:
             linhas = arquivo.readlines()
       return linhas
    #transforma as linhas em dicionario
def transf_linha_para_dicionario(linhas: list):
        linha_de_usuario = []
        lista_modelo = ['Nr','Usuário','Espaço utilizado','% do uso']

    #organizar a linhas
        for index, valor in enumerate (linhas):
            if index == 0:
                continue
            valormodificado = valor.split(';')
    #tranformar em dicionario
            dic_usuario = dict()
            for k , v in zip(lista_modelo,valormodificado):
                dic_usuario[k] = v
            linha_de_usuario.append(dic_usuario)
        return linha_de_usuario
def mostrar_infos(dic_usuario:list):
    for usuario in dic_usuario:
        print('___INFO DE USUARIOS__')
        print(f'Usuário: {usuario['Usuário']}')
        print(f'NR: {usuario['Nr']}')
        print(f'Epaço utilizado: {usuario['Espaço utilizado']}')












if __name__ == '__main__':
     linhas = manipulandoarquivo()
     print(linhas)
     dicionario_de_pessoas = transf_linha_para_dicionario(linhas= linhas )
     print(dicionario_de_pessoas)
     print(mostrar_infos(dicionario_de_pessoas))
