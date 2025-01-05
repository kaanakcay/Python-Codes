from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain

question_bank = []

for i in question_data:
    new_q = Question(i['text'], i['answer'])
    question_bank.append(new_q)

quiz = Quiz_Brain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
