from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random


question_bank = []
score = 0
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("you've completed the quiz")
print(f"your final score is {quiz.score}/{quiz.question_number}")

# game_continue = True
# while game_continue:
#     # clear()
#     question_object = random.choice(question_bank)
#     user_answer = input(f"{question_object.text} : ").lower()
#
#     if user_answer == question_object.answer.lower():
#         print("You're right")
#         print(f"The correct answer is {question_object.answer}")
#         score += 1
#         print(f"Your current score is {score}")
#
#     else:
#         print("You're wrong")
#         print(f"The correct answer is {question_object.answer}")
#         print(f"Your score is {score}")
#         game_continue = False



