from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

FERNET_KEY = os.getenv("DEVVAULT_SECRET_KEY")

cipher = Fernet(FERNET_KEY)

def encrypt_value(value: str):
    encrypted = cipher.encrypt(value.encode())
    return encrypted.decode()


def decrypt_value(value: str):
    decrypted = cipher.decrypt(value.encode())
    return decrypted.decode()