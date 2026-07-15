# 🔐 PhantomLock

> A professional Python-based file encryption tool with password authentication, SHA-256 integrity verification, and secure logging.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Version-2.0-success)

---

## 📖 Overview

PhantomLock is a command-line cybersecurity tool developed in Python that securely encrypts and decrypts files using the **Fernet symmetric encryption algorithm** provided by the `cryptography` library.

The project also includes:

- Master password authentication using **bcrypt**
- SHA-256 file integrity verification
- Secure logging
- File metadata display
- Modular project architecture
- Colorized terminal interface

This project was built to strengthen practical cybersecurity and Python programming skills.

---

# ✨ Features

- 🔐 Encrypt files securely
- 🔓 Decrypt encrypted files
- 🔑 Generate encryption keys
- 🔒 Master password authentication
- 🛡 SHA-256 integrity verification
- 📄 Display file information
- 📝 Activity logging
- 🎨 Colorized command-line interface
- 📂 Supports multiple file types
- ⚠ Error handling

---

# 📂 Project Structure

```text
PhantomLock/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── modules/
│   ├── auth.py
│   ├── decrypt.py
│   ├── encrypt.py
│   ├── file_info.py
│   ├── generate_key.py
│   ├── hash_utils.py
│   ├── logger.py
│   └── ui.py
│
├── keys/
├── logs/
├── output/
└── samples/
```

---

# ⚙ Technologies Used

- Python 3
- Cryptography (Fernet)
- bcrypt
- hashlib
- Colorama
- Logging Module
- OS Module

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/Chethana-Navin/PhantomLock---File-Encryption-Tool.git
```

Move into the project

```bash
cd PhantomLock
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```

---

# 🔄 Workflow

```text
Start
   │
   ▼
Authentication
   │
   ▼
Main Menu
   │
   ├── Generate Key
   ├── Encrypt File
   ├── Decrypt File
   └── Verify File Integrity
```

---

# 🔒 Security Features

- Fernet symmetric encryption
- Master password protection using bcrypt
- SHA-256 integrity verification
- Secure key generation
- Binary file encryption
- Activity logging

---

# 🖥 Example

```text
============================================================
              PHANTOMLOCK v2.0
============================================================

1. Generate Encryption Key
2. Encrypt File
3. Decrypt File
4. Verify File Integrity
5. Exit
```

---

# 📚 What I Learned

During this project I gained hands-on experience with:

- Python modular programming
- File handling
- Binary file processing
- Symmetric encryption
- Password hashing
- Cryptographic hashing
- Logging
- Exception handling
- Command-line interface development

---

# 🚀 Future Improvements

- Folder encryption
- Drag & Drop GUI
- Password-based encryption (PBKDF2)
- Secure file deletion
- Progress bar
- Standalone executable (.exe)

---

# 👨‍💻 Author

**Chethana Navin**

Cyber Security Undergraduate

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
