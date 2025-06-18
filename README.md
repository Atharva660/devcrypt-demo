# DevCrypt 🔐  
### Advanced Encryption Library with Devanagari Script Support

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

DevCrypt is a powerful, easy-to-use encryption library that supports traditional encryption methods alongside unique Devanagari script-based encoding.  
Perfect for developers who need robust security with cultural authenticity.

---

## ✨ Key Features

- 🔐 **AES-256-CBC Encryption**: Military-grade symmetric encryption for maximum confidentiality  
- 🧠 **Argon2id Key Derivation**: Memory-hard KDF with 64-byte random salt to resist brute-force attacks  
- 🛡️ **HMAC-SHA256 Authentication**: Ensures data integrity and detects tampering  
- 🔁 **Unique Salt & IV Per Encryption**: Prevents rainbow table and replay attacks  
- 🧩 **Dual-Layer Security**: Combines user password with a server-generated token for stronger protection  
- 🏗️ **Extensible Architecture**: Clean, modular design that’s easy to integrate into any Python project  
- ⚡ **Performance Optimized**: Fast encryption/decryption for large data  
- 🧩 **Simple API**: Intuitive interface for all skill levels  
- 🖥️ **Cross-Platform**: Works on Windows, macOS, and Linux  

---

## 🚀 Quick Start

```python
from devcrypt import DevCrypt

# Initialize encryptor
dc = DevCrypt()

# Basic encryption
encrypted = dc.encrypt("Hello World!", method="aes")
decrypted = dc.decrypt(encrypted, method="aes")

# Devanagari encoding
encoded = dc.devanagari_encode("Secret Message")
decoded = dc.devanagari_decode(encoded)
```

---

## 📦 Installation

```bash
pip install https://devcrypts.netlify.app/simple/devcrypt/devcrypt-1.0.0-py3-none-any.whl
```

---

## 🔧 Usage Examples

### 🔐 Basic Text Encryption

```python
from devcrypt import DevCrypt

dc = DevCrypt()
message = "Confidential data"
encrypted = dc.encrypt(message, method="fernet")
print(f"Encrypted: {encrypted}")
```

### 📁 File Encryption

```python
# Encrypt a file
from devcrypt import DevCrypt

def encrypt_file(input_file_path, output_file_path, user_password, server_token=None):
    dc = DevCrypt()

    if server_token is None:
        server_token = dc.generate_server_token()

    combined_secret = dc.combine_factors(user_password, server_token)

    with open(input_file_path, 'rb') as f:
        file_data = f.read()

    encrypted_data = dc.encrypt(file_data.decode('latin1'), combined_secret)

    with open(output_file_path, 'w') as f:
        f.write(encrypted_data)

    print(f"[✔] File encrypted: {output_file_path}")
    print(f"[🔐] Server token (save this!): {server_token}")
    return server_token

# Example:
password = "mySecurePassword"
token = encrypt_file("original.txt", "encrypted.txt", password)

# Decrypt a file
from devcrypt import DevCrypt

def decrypt_file(encrypted_file_path, output_file_path, user_password, server_token):
    dc = DevCrypt()
    combined_secret = dc.combine_factors(user_password, server_token)

    with open(encrypted_file_path, 'r') as f:
        encrypted_data = f.read()

    decrypted_text = dc.decrypt(encrypted_data, combined_secret)
    decrypted_data = decrypted_text.encode('latin1')

    with open(output_file_path, 'wb') as f:
        f.write(decrypted_data)

    print(f"[✔] File decrypted: {output_file_path}")

# Example:
password = "mySecurePassword"
server_token = input("🔐 Enter server token used during encryption: ")
decrypt_file("encrypted.txt", "decrypted.txt", password, server_token)
```

### 🇮🇳 Devanagari Script Encoding

```python
```

---

## 📚 Documentation

- 📥 [Installation Guide](#)
- 🚀 [Quick Start Tutorial](#)
- 🧠 [API Reference](#)
- 🧪 [Examples](#)

---

## 🎯 Use Cases

- 🌐 Web Applications: Secure user data and sessions  
- 🗃️ File Protection: Encrypt sensitive documents  
- 🇮🇳 Cultural Projects: Devanagari script preservation  
- 📖 Educational Tools: Learn encryption concepts  
- 🔐 Personal Security: Protect private information  

---

## 🏆 Why Choose DevCrypt?

| Feature              | DevCrypt | Other Libraries |
|----------------------|----------|-----------------|
| Devanagari Support   | ✅       | ❌             |
| Multiple Algorithms  | ✅       | Limited         |
| File Encryption      | ✅       | Basic           |
| Performance          | ✅ High  | Varies          |
| Documentation        | ✅ Comprehensive | Minimal |

---
# The wake-up call:
- bcrypt (1999): Vulnerable to modern GPU attacks
- Fernet: Uses basic PBKDF2 from 2013
- Most developers roll their own crypto (dangerous!)

---
# Enter DevCrypt - built for 2024's threat landscape:*

✅ *Argon2 hashing* - 100x more expensive for attackers
✅ *Memory-hard algorithm* - GPU farms become useless
✅ *Unicode optimization* - Global applications supported
✅ *2-function API* - Impossible to implement wrong

---
## 🤝 Contributing

We welcome contributions!  
Please see our **Contributing Guide** for details.

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- 📖 Documentation: [Full Docs](#)
- 🔍 Examples: [Code Examples](#)
- ❓ Issues: [GitHub Issues](#)
- 💬 Discussions: [GitHub Discussions](#)

---

⭐ If you find DevCrypt useful, please consider giving it a **star**!

Made with ❤️ for secure and culturally authentic encryption.