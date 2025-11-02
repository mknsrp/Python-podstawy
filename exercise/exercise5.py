import FreeSimpleGUI as sg

label1 = sg.Text("Enter feet:")
input1 = sg.Input()


label2 = sg.Text("Enter inches:")
input2 = sg.Input()

convert_button = sg.Button("Convert")

window = sg.Window("Converter", layout=[[label1,input1],
                                            [label2,input2],
                                            [convert_button]])
window.read()
window.close()