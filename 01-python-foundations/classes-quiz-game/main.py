from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q_data_item in question_data:
    question_text = q_data_item["text"]
    question_answer = q_data_item["answer"]
    question_bank.append(Question(question_text,question_answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")