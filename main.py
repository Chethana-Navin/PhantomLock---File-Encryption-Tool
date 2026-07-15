from modules.generate_key import generate_key
from modules.encrypt import encrypt_file
from modules.decrypt import decrypt_file
from modules.auth import setup_password, authenticate
from modules.ui import *
from modules.hash_utils import verify_hash


def display_menu():
    print("\n" + "=" * 45)
    print("         PhantomLock v1.0")
    print("      File Encryption Tool")
    print("=" * 45)
    print("1. Generate Encryption Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Verify File Integrity")
    print("5. Exit")
    print("=" * 45)


def main():
    while True:
        setup_password()

        print("=" * 40)
        print("      PHANTOMLOCK SECURITY")
        print("=" * 40)

        if not authenticate():
            print("\n❌ Incorrect password.")
            return

        success("Authentication successful!")

        banner()
        menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            generate_key()

        elif choice == "2":
            filename = input("Enter file name to encrypt: ")

            try:
                encrypt_file(filename)
            except FileNotFoundError:
                print("❌ File not found.")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "3":
            filename = input("Enter encrypted file name: ")

            try:
                decrypt_file(filename)
            except FileNotFoundError:
                print("❌ File not found.")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "4":

            filename = input("Enter file name: ")

            valid, result = verify_hash(filename)

            if valid:
                success("File integrity verified.")
                print(result)

            else:
                error("Integrity verification failed.")
                print(result)

        elif choice == "5":
            print("\nThank you for using PhantomLock.")
            info("Thank you for using PhantomLock.")
            break

        else:
            error("Invalid choice.")


if __name__ == "__main__":
    main()