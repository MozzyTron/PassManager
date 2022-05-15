import sys
import logging
import sys, pyperclip
from os import environ
from dotenv import load_dotenv
from Pass_Server import Server 

# from interface import get_user_input

load_dotenv()
# TEXT = eval(environ.get("TEXT"))


def get_user_input():
    print("Create Key: 1, Upload key: 2, Add new service and password: 3")
    command = int(input())
    if command == 1:
        pass
    if command == 2:
        pass
    if command == 3:
        s.service_name = input("Entry name of service: ")
        s.password = input("Entry password of service: ")
        


if __name__=="__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s:%(name)s:%(asctime)s:%(message)s')
    fh = logging.FileHandler('spam.log')
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.info("Pass manager started")
    s=Server()
    get_user_input()
    print(s.service_name, s.password)
    s.append_to_db()
    # s.create_key()
    # s.load_key()
    # get_user_input()
    
    