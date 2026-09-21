import json

ToDoList: dict[str, str] = {}

# reads and closes files
with open ('ToDoList.json', 'r') as file: 
    data = json.load(file)

# populates the empty dictionary with whats saved in the json
for k, v in data.items(): 
    ToDoList[k] = v



