
# Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string
# com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo,
# ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os
# caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

def embaralharar_palavra():

    palavra = list(input('informe a palavra '))

    tamanho = len(palavra)
    nova_palavra = []
    for i in range(tamanho):

       nova_palavra.append(palavra[tamanho - 1 -i])

    return''.join(nova_palavra)





    print(nova_palavra)
if __name__ == '__main__':
    print(embaralharar_palavra())