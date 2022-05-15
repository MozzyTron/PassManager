import sys

from server import *

server = Server("passwords/")

arguments = sys.argv[::-1]

if arguments[0] in ("--add", "-a"):
    service = input("Service (google, twitch, skype etc...): ").strip()
    account = input("Account (nickname or mail): ").strip()
    password = input("Enter password: ").strip()
    server.add_password(service, account, password)

elif arguments[0] in ("--get", "-g"):
    service = input("Service (google, twitch, skype etc...): ").strip()
    account = input("Account (nickname or mail): ").strip()
    server.get_password(service, account)

elif arguments[0] in ("--update_key", "-u"):
    server.update_key()

elif arguments[0] in ("--init_physical_key", "-i"):
    letter = input("Enter the physical key letter(without any punctuation): ")
    server.init_phys_key(letter)

else:
    print("Sorry, this script takes parameters. \n add - use to add password \n get - use to copy password to clipboard \n update_key - use to generate new key \n init_physical_key - use to initialize key")
