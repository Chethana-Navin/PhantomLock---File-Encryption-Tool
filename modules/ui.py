from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)


def banner():
    print(Fore.CYAN + "=" * 60)
    print(Fore.CYAN + "              PHANTOMLOCK v2.0")
    print(Fore.CYAN + "         Professional File Encryption Tool")
    print(Fore.CYAN + "=" * 60)


def menu():
    print()
    print(Fore.YELLOW + "[1]" + Style.RESET_ALL + " Generate Encryption Key")
    print(Fore.GREEN + "[2]" + Style.RESET_ALL + " Encrypt File")
    print(Fore.BLUE + "[3]" + Style.RESET_ALL + " Decrypt File")
    print(Fore.RED + "[4]" + Style.RESET_ALL + " Exit")
    print()


def success(message):
    print(Fore.GREEN + f"✔ {message}")


def error(message):
    print(Fore.RED + f"✖ {message}")


def warning(message):
    print(Fore.YELLOW + f"⚠ {message}")


def info(message):
    print(Fore.CYAN + f"ℹ {message}")