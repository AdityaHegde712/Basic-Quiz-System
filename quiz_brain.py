class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        question = self.questions_list[self.question_number]
        text = question.text
        answer = question.answer
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {text} (True/False)?: ")
        self.check_answer(answer, question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, answer, corr_answer):
        if answer.lower() == corr_answer.lower():
            self.score += 1
            print(f"You got it right!")
        else:
            print(f"You got it wrong!")
        print(f"The correct answer was: {corr_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
