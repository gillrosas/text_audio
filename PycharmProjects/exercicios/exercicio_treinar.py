#obtendo as linhas do arquivo em uma lista

# obtendo linhas do arquivo e colocando-as em uma lista.
def _read_file_to_list():
    lines = None
    with open('usuario.txt', 'r', encoding='utf-8') as _file:
        lines = _file.readlines()
    return lines


def _list_to_list_dict_user(lines_file: list):
    list_user = []
    list_labels = ['NR', 'Usuário', 'Espaço Utilizado', 'Porcentagem de Uso']

    for index, value in enumerate(lines_file):
        if index == 0:
            continue
        _values = value.split(';')

        user_dict = dict()
        for label, v in zip(list_labels, _values):
            user_dict[label] = v
        list_user.append(user_dict)

    return list_user


def _show_info(user_dict: list):
    print('____info usuario___\n')
    for user in user_dict:
        print(f"NR: {user['NR']} | Usuário: {user['Usuário']}")
        print(f'Espaço Utilizado: {user['Espaço Utilizado']}')


if __name__ == '__main__':
    # obter linhas do arquivo
    lines_file = _read_file_to_list()
    print(lines_file)
    dict_user = _list_to_list_dict_user(lines_file=lines_file)
    print(dict_user)
    print(_show_info(dict_user))