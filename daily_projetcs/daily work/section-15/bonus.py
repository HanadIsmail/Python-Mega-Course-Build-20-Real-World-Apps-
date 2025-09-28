import json

with open ("questions.json",'r') as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question ["question_text"])
    for index,option in enumerate(question["options"]):
        print(index +1 ,'-',option)
    user_choice = int (input("enter your answer: "))
    question["user_choice"] = user_choice




for index,question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score +=1
        result = "correct answer"
    else:
        result = "wrong answer"
    message = f"{index +1} {result} Your answer is {question['user_choice']},the correct answer is {question['correct_answer']}"
    print(message)


print(score ,'/', len(data))