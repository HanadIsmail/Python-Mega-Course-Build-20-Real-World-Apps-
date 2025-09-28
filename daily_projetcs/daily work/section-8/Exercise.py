#With Context Manager with Reading and Writing

with open("story.txt", "r") as file:
    store = file.read()

with open('story_copy.txt', 'w') as file:
    file.write(store)