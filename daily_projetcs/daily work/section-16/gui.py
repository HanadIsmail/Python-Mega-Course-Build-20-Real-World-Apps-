import function
import FreeSimpleGUI as sg

label = sg.Text("type in todo")
input_box = sg.InputText(tooltip = 'enter a todo')
add_button = sg.Button("add")

window = sg.Window('My todo app', layout= [[label] , [input_box,add_button]])
window.read()
window.close()