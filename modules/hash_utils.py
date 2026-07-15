import hashlib
import os


def calculate_sha256(filepath):
    """
    Calculate SHA-256 hash of a file.
    """

    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()


def save_hash(filepath):
    """
    Save SHA-256 hash to a .sha256 file.
    """

    file_hash = calculate_sha256(filepath)

    hash_file = filepath + ".sha256"

    with open(hash_file, "w") as file:
        file.write(file_hash)

    return file_hash


def verify_hash(filepath):
    """
    Verify if file hash matches stored hash.
    """

    hash_file = filepath + ".sha256"

    if not os.path.exists(hash_file):
        return False, "Hash file not found."

    with open(hash_file, "r") as file:
        stored_hash = file.read().strip()

    current_hash = calculate_sha256(filepath)

    if stored_hash == current_hash:
        return True, current_hash

    return False, current_hash