import errno
import logging
from os import environ, path
from dotenv import load_dotenv
from cryptography.fernet import Fernet


load_dotenv()
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s:%(name)s:%(asctime)s:%(message)s')

path = path.join(path.dirname(path.realpath(__file__)), "devlocal/.env")


class Server():
    def __init__(self) -> None:
        self.key = str()
        self.service_name = str()
        self.password = str()
        self.db = {}

    def create_key(self):
        self.key = Fernet.generate_key()
        with open('./mykey.key', 'wb') as mykey:
            mykey.write(self.key)
        logger.info("The key is created")

    def load_key(self):
        try:        
            with open('mykey.key', 'rb') as mykey:
                self.key = mykey.read()
                logger.info("The key is loaded")
        except:
            logger.error("The key is not found")
            return None
            # raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.key)

    def new_service_name(self):
        logger.info("Name recieved")
        return self.service_name

    def new_password(self):
        logger.info("Password recieved")
        return self.service_name

    def append_to_db(self):
        with open('test.txt', 'a+') as db:
            # self.incrypt_password(self.password)
            self.db[self.service_name] = self.password
            print(self.db)
            line = str(self.db) + "\n"
            db.write(line)

    def incrypt_password(self):
        pass

    
    def encrypt_password(self):
        pass

    def delete_service(self):
        return
    
    def start(self):
        self.new_service_name()
        self.new_password()


