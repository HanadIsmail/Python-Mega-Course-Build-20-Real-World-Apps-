import FreeSimpleGUI as sg

label1 = sg.Text("Enter feet: ")
input_box1 = sg.InputText()

label2 = sg.Text("Enter inches: ")
input_box2 = sg.InputText()

button = sg.Button("Convert")


window = sg.Window("Convertor" , layout= [[label1,input_box1], [label2,input_box2] , [button]])
window.read()
window.close()