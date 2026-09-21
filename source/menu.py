import task 
def menu() -> None:
    """This function handles the menu and the responses"""
    while True:
        print("Select an option from below:")
        print("1. Add item to list\n2. Edit item on list\n3. Remove item from list\n4. View list\n5. Quit")
    
        response = int(input())
        if response == 1:
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            name = task.Tasks(name, description)
        if response == 4:
            print('\n-----Oscars To Do List-----\n')
            task.view_list()
        if response == 5:
            break
        