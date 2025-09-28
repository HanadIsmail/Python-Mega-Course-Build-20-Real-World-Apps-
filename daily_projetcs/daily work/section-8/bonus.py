date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 9 : ")
thought = input("Let your thoughts flow : \n ")

with open(f"./files/{date}.txt" , 'w') as file:
    file.write(mood + 2 *'\n')
    file.write(thought)