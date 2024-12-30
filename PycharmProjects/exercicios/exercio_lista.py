# 12 - Foram anotadas as idades e alturas de 5 alunos.
# Faça um Programa que determine quantos alunos com mais de 13
# anos possuem altura inferior à média de altura desses alunos.
def alturadosalunos():
    alunos_todos = []
    aluno = 0
    contador = 0
    soma = 0
    while (aluno < 3):
         idade = dict()
         nome_do_aluno = input('Informe o nome do aluno: ').strip()
         idade['Nome do Aluno '] = nome_do_aluno
         ida = int(input('Informe a idade'))
         idade['Idade do aluno '] = ida

         altura = int(input('Informe a altura (em metros): '))
         idade['altura'] = altura


         alunos_todos.append(idade)
         aluno += 1
         soma += idade['altura']

    media = soma / 3
    for aluno in alunos_todos:

        if aluno['Idade do aluno '] > 13:
             contador += 1

    print(f'A quantidade de alunos com mais de 13 anos {contador} e a media total {media}')
    print(alunos_todos)

if __name__ == '__main__':
    alturadosalunos()