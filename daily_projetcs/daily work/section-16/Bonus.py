import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress")
input_box1 = sg.InputText()
button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder")
input_box2 = sg.InputText()
button2 = sg.FolderBrowse("Choose")

button3 = sg.Button("Compress")

window = sg.Window('File zipper' , layout = [[label1,input_box1, button1],[label2,input_box2, button2],[button3]])
window.read()
window.close()
