from question_model import  Question
from data import question_data
from quiz_brain import QuizBrain

logo = r"""
    ____             _             ____                         
   / __ \           (_)           |  _ \                        
  | |  | |_   _ _ __ _ _______    | |_) |_ __ __ _ _ _ __       
  | |  | | | | | '__| |_  / _ \   |  _ <| '__/ _` | | '_ \      
  | |__| | |_| | |  | |/ /  __/   | |_) | | | (_| | | | | |     
   \___\_\\__,_|_|  |_/___\___|   |____/|_|  \__,_|_|_| |_|     
"""

print(logo)


question_bank = []
for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new_question = Question(q_text,q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)



while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
