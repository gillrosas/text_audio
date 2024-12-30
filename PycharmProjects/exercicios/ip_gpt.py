





def lendo_arquivo():
    with open('iparquivos.txt', 'r', encoding='utf-8') as arq:
        linhas = arq.readlines()
    return [linha.strip() for linha in linhas]  # Remove espaços em branco

def validar_ip(ip):
    partes_do_ip = ip.split('.')  # Divide o IP em partes usando o ponto como separador

    if len(partes_do_ip) != 4:  # Verifica se há exatamente 4 partes
        return False


    for parte in partes_do_ip:
        if not parte.isdigit() or not (0 <= int(parte) <= 255):  # Verifica se está entre 0 e 255
            return False
        if parte != '0' and parte[0] == '0':  # Verifica se não tem zeros à esquerda
            return False

    return True  # Se todas as partes forem válidas, retorna True

def arquivo_v_ou_i(linhas: list):
    validos = []
    invalidos = []

    for l in linhas:
        if validar_ip(l):  # Chama a função de validação
            validos.append(l)
        else:
            invalidos.append(l)

    print("Endereços IP Válidos:", validos)
    print("Endereços IP Inválidos:", invalidos)

if __name__ == '__main__':
    linhas = lendo_arquivo()  # Lê as linhas do arquivo
    arquivo_v_ou_i(linhas)  # Valida os IPs e imprime os resultados
