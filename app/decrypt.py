from cryptography.fernet import Fernet

with open('key.key', 'rb') as key_file:
    key = key_file.read()

fernet = Fernet(key)


def decrypt_file(filename):
    with open(filename, 'rb') as file:
        encrypted_contents = file.read()

    decrypted_contents = fernet.decrypt(encrypted_contents)

    with open(filename, 'wb') as file:
        file.write(decrypted_contents)


filename = '../target.txt'
decrypt_file(filename)
