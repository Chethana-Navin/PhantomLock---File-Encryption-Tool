import os
from cryptography.fernet import Fernet
from modules.logger import log_info
from modules.file_info import display_file_info
from modules.ui import error


def load_key():
    """
    Load the encryption key from key.key
    """
    with open("key.key", "rb") as key_file:
        return key_file.read()


def decrypt_file(filename):

    display_file_info(filename)

    # Load the secret key
    key = load_key()

    # Create Fernet object
    cipher = Fernet(key)

    # Read the encrypted file
    with open(filename, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Create output filename
    # Remove .enc extension
    original_filename = filename[:-4] if filename.endswith(".enc") else filename

    # Split filename and extension
    file_name, file_extension = os.path.splitext(original_filename)

    # Create decrypted filename
    output_filename = f"{file_name}_decrypted{file_extension}"

    # Save decrypted data
    with open(output_filename, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    success("File decrypted successfully!")
    print(f"Decrypted file saved as: {output_filename}")
    
    size = os.path.getsize(filename)

    log_info(
        f"Decrypted '{filename}' | Size: {size} bytes"
    )


if __name__ == "__main__":
    filename = input("Enter the encrypted file name: ")

    try:
        decrypt_file(filename)
    except FileNotFoundError:
        error("File not found.")
    except Exception as e:
        print(f"❌ Error: {e}")