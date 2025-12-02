import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folders")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor", layout=[[label1,input1,choose_button1],
                                                  [label2, input2, choose_button2],
                                                  [compress_button]])
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folderpath = values["folders"]
    


window.close()