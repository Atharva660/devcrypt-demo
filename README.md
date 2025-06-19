# DevCrypt 🔐  
### Advanced Encryption Library with Devanagari Script Support

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

DevCrypt is a powerful, easy-to-use encryption library that supports traditional encryption methods alongside unique Devanagari script-based encoding. Perfect for developers who need robust security with cultural authenticity.

---

## ✨ Key Features

- 🔐 **AES-256-CBC Encryption**: Military-grade symmetric encryption for maximum confidentiality  
- 🧠 **Argon2id Key Derivation**: Memory-hard KDF with 64-byte random salt to resist brute-force attacks  
- 🛡️ **HMAC-SHA256 Authentication**: Ensures data integrity and detects tampering  
- 🔁 **Unique Salt & IV Per Encryption**: Prevents rainbow table and replay attacks  
- 🧩 **Dual-Layer Security**: Combines user password with a server-generated token for stronger protection  
- 🏗️ **Extensible Architecture**: Clean, modular design that's easy to integrate into any Python project  
- ⚡ **Performance Optimized**: Fast encryption/decryption for large data  
- 🧩 **Simple API**: Intuitive interface for all skill levels  
- 🖥️ **Cross-Platform**: Works on Windows, macOS, and Linux  

---

## 📦 Installation

```bash
pip install https://devcrypts.netlify.app/simple/devcrypt/devcrypt-1.0.0-py3-none-any.whl
```

---

## 🚀 Quick Start Guide

### Step 1: Basic Text Encryption

This example shows how to encrypt text and save it to files on your computer:

```python
from devcrypt import encrypt

# Your secret message
plaintext = "This is my private message"
password = "myPassword123"

# Encrypt the message
encrypted_data, token = encrypt(plaintext, password)

# Save encrypted data to your computer
with open("encrypted.txt", "w") as f:
    f.write(encrypted_data)

# Save the token separately (IMPORTANT: Keep this safe!)
with open("token.txt", "w") as f:
    f.write(token)

print("✅ Encryption complete!")
print("📁 Files created on your PC:")
print("   - encrypted.txt (contains encrypted message)")
print("   - token.txt (contains security token - keep this safe!)")
```

### Step 2: Decrypting Your Message

To decrypt your message later:

```python
from devcrypt import decrypt

# Use the same password you used for encryption
password = "myPassword123"

# Read the encrypted data from your computer
with open("encrypted.txt", "r") as f:
    encrypted_data = f.read()

# Read the token from your computer
with open("token.txt", "r") as f:
    token = f.read()

# Decrypt the message
decrypted_message = decrypt(encrypted_data, password, token)
print("🔓 Decrypted message:", decrypted_message)
```

---

## 🔄 How Data Encryption Works in DevCrypt

### The Encryption Process:
1. **Your Input**: You provide plaintext + password
2. **Token Generation**: DevCrypt creates a unique security token
3. **Key Creation**: Password + token = master key using Argon2id
4. **Encryption**: AES-256-CBC encrypts your data
5. **Output**: Two files created:
   - `encrypted.txt` - Your encrypted data
   - `token.txt` - Security token (needed for decryption)

### Security Layers:
```
Your Data → Password + Token → Argon2id Hashing → AES-256 Encryption → Encrypted File
```

---

## 📁 File Encryption Examples

### Encrypting Files on Your Computer

```python
from devcrypt import DevCrypt

def encrypt_my_file():
    dc = DevCrypt()
    
    # Generate a security token
    server_token = dc.generate_server_token()
    
    # Your password
    user_password = "mySecurePassword123"
    
    # Combine password and token for stronger security
    combined_secret = dc.combine_factors(user_password, server_token)
    
    # Read your original file
    with open("my_document.txt", 'rb') as f:
        file_data = f.read()
    
    # Encrypt the file content
    encrypted_data = dc.encrypt(file_data.decode('latin1'), combined_secret)
    
    # Save encrypted file
    with open("my_document_encrypted.txt", 'w') as f:
        f.write(encrypted_data)
    
    # Save the token (VERY IMPORTANT!)
    with open("my_document_token.txt", 'w') as f:
        f.write(server_token)
    
    print("✅ File encrypted successfully!")
    print("📁 Files on your computer:")
    print("   - my_document_encrypted.txt (encrypted version)")
    print("   - my_document_token.txt (security token)")
    print("⚠️  IMPORTANT: Keep both files safe!")
    
    return server_token

# Run the encryption
token = encrypt_my_file()
```

### Decrypting Files on Your Computer

```python
from devcrypt import DevCrypt

def decrypt_my_file():
    dc = DevCrypt()
    
    # Use the same password
    user_password = "mySecurePassword123"
    
    # Read the token from file
    with open("my_document_token.txt", 'r') as f:
        server_token = f.read()
    
    # Combine password and token
    combined_secret = dc.combine_factors(user_password, server_token)
    
    # Read encrypted file
    with open("my_document_encrypted.txt", 'r') as f:
        encrypted_data = f.read()
    
    # Decrypt the data
    decrypted_text = dc.decrypt(encrypted_data, combined_secret)
    decrypted_data = decrypted_text.encode('latin1')
    
    # Save decrypted file
    with open("my_document_decrypted.txt", 'wb') as f:
        f.write(decrypted_data)
    
    print("✅ File decrypted successfully!")
    print("📁 Decrypted file: my_document_decrypted.txt")

# Run the decryption
decrypt_my_file()
```

---

## 🌐 Sharing Encrypted Data Between Computers

### Scenario: Send encrypted data to someone else

#### On Your Computer (Sender):
```python
from devcrypt import encrypt

# Create your secret message
secret_message = "Meeting at 3 PM tomorrow"
shared_password = "ourSecretPassword2024"

# Encrypt the message
encrypted_data, token = encrypt(secret_message, shared_password)

# Save files to send
with open("secret_message.enc", "w") as f:
    f.write(encrypted_data)

with open("message_token.key", "w") as f:
    f.write(token)

print("📤 Files ready to send:")
print("   - secret_message.enc (send this file)")
print("   - message_token.key (send this file)")
print("   - Share the password separately (not in files!)")
```

#### On Recipient's Computer:
```python
from devcrypt import decrypt

# They need the same password (shared securely)
shared_password = "ourSecretPassword2024"

# Read files you sent them
with open("secret_message.enc", "r") as f:
    encrypted_data = f.read()

with open("message_token.key", "r") as f:
    token = f.read()

# Decrypt the message
secret_message = decrypt(encrypted_data, shared_password, token)
print("🔓 Received message:", secret_message)
```

---

## 📋 File Management Guide

### Files Created During Encryption:

| File Type | Purpose | Location | Share? |
|-----------|---------|----------|---------|
| `.enc` files | Contains encrypted data | Your computer | ✅ Safe to share |
| `.key` files | Contains security tokens | Your computer | ✅ Share with recipient |
| Original files | Your unencrypted data | Your computer | ❌ Keep private |

### Important Notes:
- 🔑 **Password**: Never store in files, share securely
- 📁 **Token files**: Must be shared with encrypted files  
- 💾 **Backup**: Keep copies of both encrypted and token files
- 🗑️ **Cleanup**: Securely delete original files after encryption if needed

---

## 🛡️ Security Best Practices

### Password Guidelines:
- ✅ Use at least 12 characters
- ✅ Include numbers, letters, and symbols
- ✅ Don't reuse passwords
- ❌ Don't store passwords in files

### File Handling:
- 📁 Keep token files with encrypted files
- 💾 Backup both encrypted data and tokens
- 🔒 Store backups in different locations
- 🗑️ Securely delete temporary files

---

## 🎯 Common Use Cases

### 1. Personal Document Protection
```python
# Encrypt important documents on your laptop
encrypt_file("tax_documents.pdf", "tax_documents.enc", "myPassword")
```

### 2. Secure File Sharing
```python
# Encrypt before sending via email/cloud
encrypt_file("contract.docx", "contract.enc", "sharedPassword123")
# Send .enc and .key files, share password separately
```

### 3. Backup Encryption
```python
# Encrypt backups before cloud storage
encrypt_file("family_photos.zip", "photos_backup.enc", "familyPassword")
```

---

## 🏆 Why Choose DevCrypt?

| Feature              | DevCrypt | Other Libraries |
|----------------------|----------|-----------------|
| Devanagari Support   | ✅       | ❌             |
| Multiple Algorithms  | ✅       | Limited         |
| File Encryption      | ✅       | Basic           |
| Performance          | ✅ High  | Varies          |
| Documentation        | ✅ Comprehensive | Minimal |
| User-Friendly API    | ✅       | Complex         |

---

## 🚨 The Security Wake-Up Call

### Why Modern Encryption Matters:
- **bcrypt (1999)**: Vulnerable to modern GPU attacks
- **Fernet**: Uses basic PBKDF2 from 2013
- **Most developers**: Roll their own crypto (dangerous!)

### DevCrypt - Built for 2024's Threat Landscape:
- ✅ **Argon2 hashing** - 100x more expensive for attackers
- ✅ **Memory-hard algorithm** - GPU farms become useless
- ✅ **Unicode optimization** - Global applications supported
- ✅ **2-function API** - Impossible to implement wrong

---

## 🔧 Advanced Usage

### Custom Token Management
```python
from devcrypt import DevCrypt

dc = DevCrypt()

# Generate your own token
custom_token = dc.generate_server_token()
print(f"Custom token: {custom_token}")

# Use custom token
password = "myPassword"
combined_key = dc.combine_factors(password, custom_token)
```

### Batch File Processing
```python
import os
from devcrypt import DevCrypt

def encrypt_folder(folder_path, password):
    dc = DevCrypt()
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            encrypted_path = file_path + '.enc'
            token_path = file_path + '.key'
            
            # Encrypt each file
            token = encrypt_file(file_path, encrypted_path, password)
            
            # Save token
            with open(token_path, 'w') as f:
                f.write(token)
            
            print(f"✅ Encrypted: {filename}")

# Usage
encrypt_folder("./documents", "folderPassword123")
```

---

## 🤝 Contributing

We welcome contributions! Please see our **Contributing Guide** for details.

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🔗 Useful Links

- 📖 Documentation: [Full Documentation](https://github.com/Atharva660/devcrypt-demo/blob/main/README.md)
- 🔍 Examples: [Usage Examples](https://github.com/Atharva660/devcrypt-demo/tree/main/examples)
- ❓ Issues: [GitHub Issues](https://github.com/Atharva660/devcrypt-demo/issues)

---

## 📞 Support

Need help? Here are your options:
- 📧 Email: support@devcrypt.com
- 💬 Discord: [DevCrypt Community](#)
- 📖 Wiki: [Documentation Wiki](#)

---

⭐ If you find DevCrypt useful, please consider giving it a **star**!

Made with ❤️ for secure and culturally authentic encryption.