import os
import mimetypes


def get_file_type(filepath):
    file_type, _ = mimetypes.guess_type(filepath)

    if file_type:
        return file_type

    return "Unknown"

def get_file_info(filepath):
    """
    Returns information about a file.
    """

    if not os.path.exists(filepath):
        return None

    file_name = os.path.basename(filepath)
    file_extension = os.path.splitext(filepath)[1]
    file_size = os.path.getsize(filepath)
    file_location = os.path.abspath(os.path.dirname(filepath))

    return {
        "name": file_name,
        "extension": file_extension if file_extension else "No Extension",
        "size": file_size,
        "location": file_location
    }


def format_file_size(size):
    """
    Convert bytes into KB, MB, GB...
    """

    for unit in ["Bytes", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"


def display_file_info(filepath):
    info = get_file_info(filepath)

    if info is None:
        print("\n❌ File not found.\n")
        return

    print("\n" + "=" * 50)
    print("              FILE INFORMATION")
    print("=" * 50)
    print(f"Name      : {info['name']}")
    print(f"Extension : {info['extension']}")
    print(f"Type      : {get_file_type(filepath)}")
    print(f"Size      : {format_file_size(info['size'])}")
    print(f"Location  : {info['location']}")
    print("=" * 50)