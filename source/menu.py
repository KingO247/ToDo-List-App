import MenuLogic
def menu() -> None:
    """This function handles the menu and the responses"""
    while True:
        print("Select an option from below:")
        print("1. Add item to list\n2. Edit item on list\n3. Remove item from list\n4. View list\n5. Quit")
    
        response = int(input())
        if response == 1:
            MenuLogic.response_1()
        if response == 2:
            MenuLogic.response_2()
        if response == 4:
            MenuLogic.response_4()
        if response == 5:
            MenuLogic.response_5()
            break
        