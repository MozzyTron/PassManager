import json
from os.path import exists
from os import makedirs
from string import ascii_uppercase as alphabet
from sys import exit

import pyperclip

from encryptor import *

encryptor = Encryptor()


class Server():

    def __init__(self, passwords_loc="") -> None:
        try:
            makedirs(passwords_loc)
        except FileExistsError:
            pass#directory already exists 
        self.passwords_loc = passwords_loc + "passwords"

    def get_passwords(self):
        self.check_physical_key()
        if not exists(self.passwords_loc):
            return {}

        return json.loads(encryptor.file_decrypt(self.key, self.passwords_loc, None, retval="text").replace("'", '"'))

    def save_passwords(self, passwords):
        self.check_physical_key()

        encryptor.file_encrypt(
            self.key, None, self.passwords_loc, str(passwords))
        return "OK"

    def add_password(self, service, account, password):

        passwords = self.get_passwords()

        if service in passwords:
            passwords[service][account] = password
        else:
            passwords[service] = {account: password}

        if not self.save_passwords(passwords):
            print("Can't find physical key")

        print("New password successfully saved!")

    def get_password(self, service, account):

        passwords = self.get_passwords()

        try:

            password = passwords[service][account]
            pyperclip.copy(password)
            print("Copied to clipboard!")

        except:
            print("No such password found")

    def update_key(self):
        self.check_physical_key()

        old_key = encryptor.key_load(self.key_loc)
        new_key = encryptor.key_create()
        encryptor.file_decrypt(old_key, self.passwords_loc, self.passwords_loc)
        encryptor.file_encrypt(new_key, self.passwords_loc, self.passwords_loc)
        encryptor.key_write(new_key,self.key_loc)
        print("Key updated successfully")

    def check_physical_key(self):
        print("Detecting physical key...")
        for i in alphabet:
            if exists(loc := f"{i}:/TOPSECRETKEYFOLDER/KEY.key"):
                print("Physical key found!")
                self.key = encryptor.key_load(loc)
                self.key_loc = loc
                return True
        print("Can't find physical key")
        exit()

    def init_phys_key(self, letter):
        try:
            makedirs(f"{letter}:/TOPSECRETKEYFOLDER/")
            encryptor.key_write(encryptor.key_create(),
                                letter+":/TOPSECRETKEYFOLDER/KEY.key")
        except Exception as e:
            print("Initialization failed due to the error: "+str(e))
        else:
            print("Key initialized successfully")
