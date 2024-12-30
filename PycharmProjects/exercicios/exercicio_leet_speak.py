def investigacao():
   perguntas = [
       "Telefonou para a vítima?",
       "Esteve no local do crime?",
       "Mora perto da vítima?",
       "Devia para a vítima?",
       "Já trabalhou com a vítima?"
   ]


   verdadeira_resposta = 0
   for pergunta in perguntas:
       resposta = input((pergunta) + ' Digite sim e não: ').strip().lower()
       if resposta == 'sim':
           verdadeira_resposta +=1


   if verdadeira_resposta == 2:
       reu = 'Suspeito'
   elif 3 <= verdadeira_resposta <=4:
       réu = 'Complice'
   elif verdadeira_resposta == 5:
       reu = 'Culpado pelo fato'
   else:
       reu = 'Inocente'
   print(f"Essa pessoa é: {reu}")


if __name__=='__main__':
   investigacao()

