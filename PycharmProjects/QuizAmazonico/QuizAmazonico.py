import tkinter
#Importar todas a bibliotecas

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import json

#1. Fazer uma classe para rodar o meu quiz(onde vai ter perguntas respostas, botões)
class Quiz:
    def __init__(self):  #a função init é onde vamos colocar todas as subclases que estão na classe de quiz
        self.q_no = 0
        self.display_title()   #1
        self.display_question()
        self.buttons()

        self.opt_selected = IntVar()
        self.opts = self.radio_button() #o opção opts vai recber o valor da funçã radio_button para percorrer a lista
        self.display_option()


        self.correct = 0
        self.perguntas_do_quiz_size = len(question)


    def display_title(self):   #1.aqui vou construir a interface para interação e fazendo o self para dizer que representa a classe do quiz
        title = Label(gui, text= "QUIZ AM", width= 800, height= 2, bg = "green", fg="orange", font= ("Times New Rome", 20, "bold") )
        title.pack()

    def display_question(self):  #2 aqui vamos mostrar as questões que estão no arquivo json
        q_no= Label(gui, text = question[self.q_no], font = ("arial", 12, "bold"), anchor = "w") # a variavel queston está no arquivo jso, preciso chamr
        q_no.pack()

    def display_option(self):  #3 vamos mostrar as opções para a pessoa escolher
        valor = 0   #como está em uma lista vamos precisar percorrer
        self.opt_selected.set(0) #aqui sera criada uma variavel para selecionar a opções

        #precisamos percorrer as opções que estão na lista la no json
        for option in options[self.q_no] :
            self.opts[valor]["text"] = option
            valor +=1


    def radio_button(self):   #4 fazer o botão para as opções
        option_list = []

        first_option_position = 150

        #precisamos fazer um loop para que as opções possa aparecer
        while len(option_list) < 4: #existem 4 opções de respostas no json
            radio_btn = ttk.Radiobutton(gui,text=" ", variable= self.opt_selected, value= len(option_list)+1)

        option_list.append(radio_btn)
        radio_btn.place(x=100, y = first_option_position)

    def check_ans(self,q_no):
        if self.opt_selected == answer[q_no]:
            return True

    def display_result (self):   #7.fazer a tela final
        wrong_count = self.perguntas_do_quiz_size - self.correct
        correct = f"Respostas corretas {self.correct}"
        wrong = f"Respostas erradas: {wrong_count}"

        score = (self.correct / self.perguntas_do_quiz_size *100)
        result = f"Pontos acumulados: {score}"
        mb.showinfo("Resultado", f"{result}\n{correct}\n{wrong}")






    def next_btn(self): #conseguri manipular para as proximas questões
        if self.check_ans(self.q_no):   #checar se esta correta a respostas na funcao check_ans
            self.correct += 1
        self.q_no += 1

        if self.q_no == self.perguntas_do_quiz_size:
            self.display_result() #uma funcao para mostrar
            gui.destroy()
        else:
            self.display_question()
            self.display_option()


    def buttons(self):     #5. colocar os botões de proximo e sair
        next_button = tkinter.Button(gui, text = "Próximo", command= self.next_btn, width= 15) #criar a função next_btn
        next_button.place(x=700, y=380)

        quit_button = tkinter.Button(gui, text= "Sair", command= gui.destroy, width=10)
        quit_button.place(x=50, y=380)






#tratando os dados do meu arquivo json
with open("perguntas_do_quiz.json", "r", encoding="utf-8") as f:
    perguntas_do_quiz = json.load(f)

question = (perguntas_do_quiz["perguntas"])
options = (perguntas_do_quiz["opcoes"])
answer = (perguntas_do_quiz["respostas_correta"])




if __name__ == "__main__":
    # Construir a janela com tkinter
    gui = Tk()  # instancia o tkinter para variavel gui
    gui.title("   Quiz Amazonico  ")
    gui.geometry("800x350")  # defifne a geometria
    gui.resizable(width=False, height=False)
    #Instanciar a classeQuiz
    quiz = Quiz()

    gui.mainloop()  # adiciona o loop para rodar aaplicação