import FreeSimpleGUI as sg

from zip_extractor import extract_archive

"""Here, we have chosen FileBrowse instead of FilesBrowse 
because we are selecting a single file.
"""
sg.theme("Black")
label_1 = sg.Text("Select archive: ")
input_1 = sg.Input()
choose_button_1 = sg.FileBrowse("Choose", key="archive")

label_2 = sg.Text("Select destination directory: ")
input_2 = sg.Input()
choose_button_2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key = "output", text_color="green")

window = sg.Window("Archive Extractor",
                   layout = [[label_1, input_1, choose_button_1],
                             [label_2, input_2, choose_button_2],
                             [extract_button, output_label]])
while True:
    event, values = window.read()
    match event:
        case sg.WINDOW_CLOSED:
            break
    archivepath = values['archive']
    dest_dir = values['folder']
    extract_archive(archivepath, dest_dir)
    window["output"].update(value= "Extraction Completed!")


window.close()