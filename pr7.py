MORZE = {'a': '.-', 'b': '-…', 'c': '-.-.', 'd': '-..',
 'e': '.', 'f': '..-.', 'g': '--.', 'h': '….',
 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
 'q': '--.-', 'r': '.-.', 's': '…', 't': '-',
 'u': '..-', 'v': '…-', 'w': '.--', 'x': '-..-',
 'y': '-.--', 'z': '--..'}


def encrypt_word(word):
    encrypted = []
    for letter in word:
        encrypted.append(MORZE[letter])

    return ''.join(encrypted)

def encrypt_message(message):

    words = message.split()

    encrypted_message = [encrypt_word(word) for word in words]
    return encrypted_message


def start():

    message = str(input('')).lower()
    encrypted_message = encrypt_message(message)
    print('\n'.join(encrypted_message))


if __name__ == '__main__':
    start()