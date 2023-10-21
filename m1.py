from PyQt5.QtWidgets import QApplication
#------------------------
#урок 3
from random import choice, shuffle
from time import sleep
#------------------------
app = QApplication([])
from m2 import *
from m3 import *
#------------------
#урок3
class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2,
                 wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask += 1
q1 = Question('в каком году випущена ігра Fortnite', '2017', '2000', '1941', '2013')
q2 = Question('что означає слово хайграунд', 'позіция више', 'позіция ниже', "восполнять здоров'я", 'попаденія прямо в голову')
q3 = Question('как восполнить блакитний хіл', '2мініка і 1бігу', '4мініка', 'аптечка', '10грибов')
q4 = Question('какая щяс глава', '4', '1', '3', '5')
q5 = Question('в каком году Fortnite був самим популярним в міре', '2022', '2017', '2011', '2023')
q6 = Question('чи в Fortnite можна грати з телефона', 'так', 'ні', 'так 30мин', '5')
q7 = Question('чи була колаба з nike', 'так', 'ні', 'незнаю', 'так 5хвилин назад')
q8 = Question('какой щяс сезон', '26', '1', '24', '36')
q9 = Question('какой тематики щяс сезон', 'шпіонский', 'крутой', 'космический', 'гонки')
q10 = Question('скоко стойт бп', '950вб', '200вб', '1200вб', '1500вб')

radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

def new_question():
    global cur_q
    cur_q= choice(questions)
    lb_question.setText(cur_q.question)
    lb_right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)

    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)
new_question()
def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                lb_result.setText('Правильно!')
                answer.setChecked(False)
                break
    else:
        lb_result.setText('Неправильно!')
    RadioGroup.setExclusive(True)
def click_ok():
    if btn_next.text() == 'Відповісти':
        check()
        gb_question.hide()
        gb_answer.show()
        btn_next.setText('Наступне запитання')
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()

        btn_next.setText('Відповісти')
btn_next.clicked.connect(click_ok)
def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show()
btn_rest.clicked.connect(rest)
def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
btn_clear.clicked.connect(clear)
def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(), le_wrong_ans1.text(), le_wrong_ans2.text(), le_wrong_ans3.text())
    questions.append(new_q)
    clear()
btn_add_question.clicked.connect(add_question)


def menu_generation():
    menu_win.show()
    window.hide()
btn_menu.clicked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    window.show()
btn_back.clicked.connect(back_menu)
window.show()
app.exec_()