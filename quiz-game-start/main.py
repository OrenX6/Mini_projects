from data import question_data  # list of dict
from question_model import Question  # class
from quiz_brain import QuizBrain  # class

question_bank = []  # list of Question objects
for question in question_data:  # loop through each dictionary in the list and accesses specific values.
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)  # create an instance of the class.

while quiz.still_has_question():
    quiz.next_question()
else:
    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
