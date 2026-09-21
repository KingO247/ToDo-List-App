import json

ToDoList: dict[str, str] = {}

def populate() -> None:
    try:
        # reads and closes files
        with open ('ToDoList.json', 'r') as file:
            content = file.read().strip()
            if not content:
                return 
            data = json.loads(content)
    except FileNotFoundError:
        return

    # populates the empty dictionary with whats saved in the json
    for k, v in data.items(): 
        ToDoList[k] = v


def save() -> None:
    with open ("ToDoList.json", "w") as file:
        json.dump(ToDoList, file)
