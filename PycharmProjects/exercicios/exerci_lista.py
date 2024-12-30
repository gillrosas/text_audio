# 16 - Utilize uma lista para resolver o problema a seguir.
# Uma empresa paga seus vendedores com base em comissões.
# O vendedor recebe $200 por semana mais 9 por cento de suas
# vendas brutas daquela semana.
# Por exemplo, um vendedor que
# teve vendas brutas de $3000 em uma semana recebe $200 mais 9
# por cento de $3000, ou seja, um total de $470.
# Escreva um programa (usando um array de contadores) que determine quantos
# vendedores receberam salários nos seguintes intervalos de valores:
#
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
#
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário,
# sem fazer vários ifs aninhados.
# '''

def vendedores():
    lista_vend = []
    contador = 0

    while True:
       vendedor = input('Informe o nome do vendendor ou aperte ENTER para sair: ')
       if not vendedor:
           break
       nome_vendedor = dict()
       nome_vendedor['vendedor'] = vendedor

       salario = float(input('Informe o salario: '))
       nome_vendedor['salario'] = salario
       lista_vend.append(nome_vendedor)

       novo_salario = (200 + (1.9*salario))
       nome_vendedor['novo salario'] = novo_salario
    print(lista_vend)


    for ven in lista_vend:
        if 900 <=ven.get('novo salario')<= 999:
            contador += 1
    print(contador)








if __name__ == '__main__':
     vendedores()