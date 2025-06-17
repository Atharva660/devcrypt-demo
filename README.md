# DevCrypt 🔐  
### Advanced Encryption Library with Devanagari Script Support

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

DevCrypt is a powerful, easy-to-use encryption library that supports traditional encryption methods alongside unique Devanagari script-based encoding.  
Perfect for developers who need robust security with cultural authenticity.

---

## ✨ Key Features

- ✅ **Multi-Algorithm Support**: AES, RSA, Fernet, and custom algorithms  
- 🇮🇳 **Devanagari Encoding**: Unique script-based encryption for cultural projects  
- 📁 **File Encryption**: Secure any file type with ease  
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
pip install --index-url https://devcrypts.netlify.app/simple/ devcrypt
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
dc.encrypt_file("document.pdf", "document_encrypted.pdf")

# Decrypt a file
dc.decrypt_file("document_encrypted.pdf", "document_restored.pdf")
```

### 🇮🇳 Devanagari Script Encoding

```python
# Encode using Devanagari characters
text = "Secret message"
encoded = dc.devanagari_encode(text)
print(f"Encoded: {encoded}")  # Output in Devanagari script
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