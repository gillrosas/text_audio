# #Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
# contendo um relatório dos endereços IP válidos e inválidos.
# O arquivo de entrada possui o seguinte formato:

#fazer a função que ler o arquivo
def ler_arquivo():
    with open('iparquivos.txt','r', encoding= 'utf-8') as arquivo:
        linhas = arquivo.readlines()

    return [linha.strip() for linha in linhas]

#fazer a validaação do ip
def validar_ip(ip):
    parte_ip = ip.split('.')

    if len(parte_ip) != 4:
        return False
    for parte in parte_ip:
        if not parte.isdigit() or not (0<= int(parte) <= 255):
           return False
        if parte == '0' and parte[0] == '0':
            return False
    return True
#fazer a função para validar ip no arquivo
def validar_linhas_do_arquivo(linhas: list):
    validos = []
    invalidos = []
    for l in linhas:
        if validar_ip(l):
            validos.append(l)
        else:
            invalidos.append(l)
    print('[Endereços Válidos]')
    for val in validos:
        print(f'{val}')
    print('[Endereços Inválidos]')
    for ival in invalidos:
        print(f'{ival}')


if __name__ == '__main__':
    lines = ler_arquivo()
    validar_linhas_do_arquivo(linhas=lines)