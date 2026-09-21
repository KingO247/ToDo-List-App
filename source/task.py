from Memory import ToDoList

def view_list() -> str:
        """Will print the current list of task names and descriptions"""
        i = 0
        for k, v in ToDoList.items():
            i += 1
            print(f'{i}. {k}: {v}\n')
class Tasks:
    """This class will handle the initialization, removal, viewing, state of, and editing of tasks"""
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        ToDoList[name] = description
    
    def edit(self, name: str, description: str) -> None:
        ToDoList[name] = description


            

