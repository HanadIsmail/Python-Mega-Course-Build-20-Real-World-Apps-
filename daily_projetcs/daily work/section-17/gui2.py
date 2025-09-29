import function
import FreeSimpleGUI as sg

label = sg.Text("type in todo")
input_box = sg.InputText(tooltip = 'enter a todo', key = 'todos')
add_button = sg.Button("add")

window = sg.Window('My todo app', layout= [[label] , [input_box,add_button]], font = ('Helvetica' , 20))

while True:
    event , values = window.read()
    print(event)
    print(values)
    match event:
        case 'add':
            todos = function.get_todos()
            new_todo = values['todos'] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close()