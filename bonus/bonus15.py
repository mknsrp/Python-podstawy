import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)


for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index + 1} - {alternative}")
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score +=1
        result = "Correct answer"
    else:
        result = "Wrong answer"
    message = (f"{result} - Your answer for {index + 1} question is: {question['user_choice']}"
               f", Correct answer: {question['correct_answer']}")
    print(message)
print(f"Your score is {score}/{len(data)}")



