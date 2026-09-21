import MenuLogic
import FreeSimpleGUI as sg
def menu() -> None:
    """This function handles the menu and the responses"""
    layout = [
        [sg.Button("Add Item"), sg.Button("Edit Item")],
        [sg.Button("Remove"), sg.Button("View")],
        [sg.Button("Quit")],
    ]
    window = sg.Window("Oscar's To Do List", layout)
    while True:
        event, _values = window.read()
        if event in (sg.WIN_CLOSED, "Quit"):
            MenuLogic.response_5()  # save
            break
        if event == "Add":
            MenuLogic.response_1()
        elif event == "Edit":
            MenuLogic.response_2()
        elif event == "Remove":
            MenuLogic.response_3()
        elif event == "View":
            MenuLogic.response_4()
    window.close()
        