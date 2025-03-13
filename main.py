import sys
import string
args = sys.argv[1::]
num_args = len(args)
if (num_args != 3):
    print("not allowed")
    exit()

alphabet = list(string.ascii_uppercase)
# print(alphabet)

encrypt = (args[0] == 'e')
# key = int(args[1])
# print(key)
msg = args[2]

def encrypt_alg(msg, key):
    new = []
    for idx, msg_char in enumerate(list(msg)):
        new.append(alphabet[(alphabet.index(msg_char) + key) % 26])
    return "".join(new)

def decrypt_alg(msg, key):
    new = []
    for idx, msg_char in enumerate(list(msg)):
        new.append(alphabet[(alphabet.index(msg_char) - key) % 26])
    return "".join(new)

if (encrypt):
    encrypted_msg = encrypt_alg(msg, int(args[1]))
    print(encrypted_msg)
else:
    decrypted_msg = decrypt_alg(msg, int(args[1]))
    print(decrypted_msg)
    # for key in range(0,27):
    #     print(f"key: {key} | output: {decrypt_alg(args[2], key)}")
