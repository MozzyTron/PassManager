import sys, pyperclip
from dotenv import load_dotenv
from os import environ

TEXT = {'steam': "pass1", 'vk': "pass2", 'cloud': "pass3"}

load_dotenv()
TEXT = eval(environ.get("TEXT"))


def get_user_input():
    if len(sys.argv)==0:
        print("Welcome to the Password Manager")

    if len(sys.argv) < 2:
        print('Usage: py mclip.py [keyphrase] - copy phrase text')
        sys.exit()

    keyphrase = sys.argv[1] # first command line arg is the keyphrase

    if keyphrase in TEXT:
        pyperclip.copy(TEXT[keyphrase])
        print('Text for ' + keyphrase + ' copied to clipboard.')

    else:
        print('There is no text for ' + keyphrase)

get_user_input()

class Encryptor():

    def key_create(self):
        key = Fernet.generate_key()
        return key

    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key


    def file_encrypt(self, key, original_file, encrypted_file):
        
        f = Fernet(key)

        with open(original_file, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open (encrypted_file, 'wb') as file:
            file.write(encrypted)

    def file_decrypt(self, key, encrypted_file, decrypted_file):
        
        f = Fernet(key)

        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(decrypted_file, 'wb') as file:
            file.write(decrypted) 
