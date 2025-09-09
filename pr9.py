FILE_TYPES = {}

ACTION_TYPES = {"r": "read",
                "w": "write",
                "x": "execute"}

def format_actions(actions):
    return [ACTION_TYPES[action] for action in actions]

def set_types(file, actions):
    formatted_actions = format_actions(actions)
    FILE_TYPES[file] = formatted_actions

def is_allowed(file, action):
    #print(file, action)
    return 'OK' if action in FILE_TYPES[file] else 'Access denied'

def parse_file(data):
    files_number = int(data[0]) + 1
    [set_types(line.split()[0], line.split()[1:]) for line in data[1:files_number]]
    #print(json.dumps(FILE_TYPES, indent=4))
    actions_number = int(data[files_number])
    #print(actions_number)
    [print(is_allowed(line.split()[1], line.split()[0])) for line in data[files_number + 1:]]



def start():
    with open("files.txt", "r") as f:
        data = f.read().splitlines()

    parse_file(data)

if __name__ == "__main__":
    start()