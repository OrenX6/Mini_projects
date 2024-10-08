class QuizBrain:
    def __init__(self, question_data):
        self.question_list = question_data  # list of questions objects
        self.question_number = 0  # default attribute value
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]  # current question object
        self.question_number += 1
        guess = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ")
        self.check_answer(guess, current_question.answer)

    def still_has_question(self):
        """
        track the question_number attribute and check if we still have questions at the bank.
        :return: True or False
        """
        return self.question_number < len(self.question_list)

    def check_answer(self, user_guess, correct_answer):
        if user_guess.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right !")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score  is: {self.score}/{self.question_number}")
        print("\n")
