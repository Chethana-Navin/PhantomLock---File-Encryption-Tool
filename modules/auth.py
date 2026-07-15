import bcrypt
import os
from getpass import getpass

PASSWORD_FILE = "keys/master.hash"


def setup_password():
    """
    Create a master password on first run.
    """

    if os.path.exists(PASSWORD_FILE):
        return

    print("\n========== First Time Setup ==========\n")

    while True:
        password = getpass("Create a master password: ")
        confirm = getpass("Confirm password: ")

        if password != confirm:
            print("\n❌ Passwords do not match.\n")
            continue

        if len(password) < 8:
            print("\n❌ Password must be at least 8 characters.\n")
            continue

        hashed_password = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )

        with open(PASSWORD_FILE, "wb") as file:
            file.write(hashed_password)

        print("\n✅ Master password created successfully!\n")
        break


def authenticate():
    """
    Verify the master password.
    """

    with open(PASSWORD_FILE, "rb") as file:
        stored_password = file.read()

    password = getpass("Enter Master Password: ")

    return bcrypt.checkpw(
        password.encode(),
        stored_password
    )