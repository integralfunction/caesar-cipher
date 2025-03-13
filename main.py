import string
import argparse

alphabet: list = list(string.ascii_uppercase)


def left_shift(message: str, key: int):
    new = []
    for char in list(message):
        new_index = alphabet.index(char) - key
        new.append(alphabet[new_index % 26])
    return "".join(new)


def right_shift(message: str, key: int):
    new = []
    for char in list(message):
        new_index = alphabet.index(char) + key
        new.append(alphabet[new_index % 26])
    return "".join(new)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='main.py',
        description='Simple Caesar Cipher. Only supports uppercase!')
    parser.add_argument('crypt', help='to encrypt or decrypt',
                        choices=('encrypt', 'decrypt'))
    parser.add_argument('key', help='how much to shift by', type=int)
    parser.add_argument('message', type=str)
    args = parser.parse_args()

    crypt: str = args.crypt
    key: int = args.key
    message: str = args.message

    if (not message):
        print("Message can't be empty")
        return
    if (key < 0):
        print("key can't be negative")
        return
    if (crypt == 'encrypt'):
        print(right_shift(message, key))
    else:
        print(left_shift(message, key))


if __name__ == '__main__':
    main()
