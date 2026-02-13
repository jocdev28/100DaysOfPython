from question_model import Question
from data import question_data

question_bank = []

# for question in question_data:
#     question_bank.append(Question(question["text"], question["answer"]))
#
# print(question_bank)

for index in range(len(question_data)):
    current_question = question_data[index]
    question_bank.append([current_question["text"], current_question["answer"]])

print(question_bank)
