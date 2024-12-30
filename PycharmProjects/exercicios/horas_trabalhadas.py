# 1 - Faça um Programa que pergunte quanto você ganha por hora e o número de
# horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
from functools import total_ordering


def conta_salario():
    ganhos_por_horas = float(input('Informe o seus ganhos por hora '))
    numeros_de_horas_trabalhadas = float(input('Informe as horas trabalhadas no mês '))

    total = ganhos_por_horas * numeros_de_horas_trabalhadas

    return total

if __name__ == '__main__':
    print('O seu ganho mensal: ',conta_salario())


