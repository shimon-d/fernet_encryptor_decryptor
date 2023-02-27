from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

with open('key.key', 'w') as file:
    file.write(key.decode('utf-8'))


def encrypt_file(filename):
    with open(filename, 'rb') as file:
        file_contents = file.read()

    encrypted_contents = fernet.encrypt(file_contents)

    with open(filename, 'wb') as file:
        file.write(encrypted_contents)


filename = '../target.txt'
encrypt_file(filename)
