import os
from cryptography.fernet import Fernet
from modules.logger import log_info
from modules.file_info import display_file_info
from modules.ui import success
from modules.hash_utils import save_hash


def load_key():
    """
    Load the encryption key from key.key
    """
    with open("key.key", "rb") as key_file:
        return key_file.read()


def encrypt_file(filename):

    display_file_info(filename)

    # Load the secret key
    key = load_key()

    # Create Fernet object
    cipher = Fernet(key)

    # Read the original file
    with open(filename, "rb") as file:
        file_data = file.read()

    # Encrypt the data
    encrypted_data = cipher.encrypt(file_data)

    # Save encrypted data
    directory = os.path.dirname(filename)
    base_name = os.path.basename(filename)

    encrypted_filename = os.path.join(directory, base_name + ".enc")

    with open(encrypted_filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    hash_value = save_hash(filename)

    print("\nSHA-256:")
    print(hash_value)

    success("File encrypted successfully!")
    print(f"Encrypted file saved as: {encrypted_filename}")
    
    size = os.path.getsize(filename)

    log_info(
        f"Encrypted '{filename}' | Size: {size} bytes"
    )


if __name__ == "__main__":
    filename = input("Enter the file name to encrypt: ")

    try:
        encrypt_file(filename)
    except FileNotFoundError:
        print("❌ File not found.")
    except Exception as e:
        print(f"❌ Error: {e}")