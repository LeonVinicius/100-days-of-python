class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        c_question = self.question_list[self.question_number]
        self.question_number +=1
        u_answer = input(f"Q.{self.question_number}: {c_question.text} (True/False): ")
        self.check_question(u_answer, c_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_question(self, u_answer , c_question):
        if u_answer.lower() == c_question.lower():
            self.score += 1
            print("You got it right! ")
        else:
            print("That's wrong. ")
        print(f"The correct answer was: {c_question}")
        print(f"Your current score is: {self.score}/{self.question_number }")
        print("\n")
