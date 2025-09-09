def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


def modulus(a, b):
    if b == 0:
        raise ValueError("Modulus by zero is not allowed")
    return a % b


def absolute(a, b):
    return abs(a), abs(b)


def power(a, b):
    return a ** b


def ensure_input(a, b):
    try:
        float(a)
        float(b)
        return True
    except ValueError:
        print("The two inputs should be floats or ints.")
        return False


def start():
    actions = {
        "+": addition,
        "-": subtraction,
        "*": multiplication,
        "/": division,
        "%": modulus,
        "abs": absolute,
        "pow": power,
    }

    try:
        data = input("Enter two numbers and operation (e.g., 5 3 +): ").split()

        if len(data) != 3:
            print("Invalid input. Please enter: number number operation")
            return

        a_str, b_str, action = data

        if not ensure_input(a_str, b_str):
            return

        a = float(a_str)
        b = float(b_str)

        if action not in actions:
            print(f"Invalid operation. Available operations: {list(actions.keys())}")
            return

        result = actions[action](a, b)
        print(f'{a} {action} {b} = {result}')

    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    start()