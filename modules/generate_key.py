from cryptography.fernet import Fernet
from modules.logger import log_info

def generate_key():
    key = Fernet.generate_key()

    with open("key.key", "wb") as key_file:
        key_file.write(key)

    print("Encryption key generated successfully!")
    log_info("Encryption key generated.")

if __name__ == "__main__":
    generate_key()