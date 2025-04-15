import FreeSimpleGUI as sg


label_1 = sg.Text("Enter feet:")
input_1 = sg.Input()

label_2 = sg.Text("Enter inches:")
input_2 = sg.Input()

convert_button = sg.Button("Convert")
output_label = sg.Text("", key="output")



window = sg.Window("Convertor", layout=[[label_1, input_1],
                                        [label_2, input_2],
                                        [convert_button, output_label]
                                        ])
window.read()
window.close()