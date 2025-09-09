USERS = {}

def is_user(username):
    return username in USERS

def get_status(username):
    if not is_user(username):
        USERS[username] = 0
        return 'OK'

    USERS[username] += 1
    return f'{username}{USERS[username]}'


def start():
    with open("users.txt", "r") as f:
        users = f.read().splitlines()[1:]

    [print(get_status(username)) for username in users]


if __name__ == "__main__":
    start()
