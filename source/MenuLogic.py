import task
import Memory

def response_1() -> None:
    name = input("Enter item name: ")
    name = name.upper()
    description = input("Enter item description: ")
    name = task.Tasks(name, description)

def response_2() -> None:
    task.view_list()
    selection = input("Enter name of item to edit")
    selection = selection.upper()
    new_desc = input("Enter new description for item: ")
    task.edit(selection,new_desc)

def response_3() -> None:
    pass


def response_4() -> None:
    print('\n-----Oscars To Do List-----\n')
    task.view_list()

def response_5() -> None:
    Memory.save()