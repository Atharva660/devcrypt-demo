
# DevCrypt - Quick Start Guide

Get up and running with DevCrypt in minutes!

---

## 🔐 Your First Encryption

Encrypt and decrypt using your password and a server-generated token:

```python
from devcrypt import encrypt, decrypt

# Encrypt
plaintext = "Hello, DevCrypt!"
password = "MyStrongPassword123"
encrypted_data, token = encrypt(plaintext, password)
print("Encrypted:", encrypted_data)
print("Token:", token)

# Decrypt
decrypted_text = decrypt(encrypted_data, password, token)
print("Decrypted:", decrypted_text)
```

---

## 💡 Basic Concepts

### 1. Initialization

```python
from devcrypt import DevCrypt

dc = DevCrypt()  # Initializes core class
```

### 2. Password + Token Security

DevCrypt requires both a password and a server-generated token to encrypt and decrypt. This dual-layer security makes brute-force much harder.

```python
combined = dc.combine_factors("user_password", "server_token")
```

### 3. Encryption with Combined Secret

```python
combined = dc.combine_factors("user_password", "server_token")
encrypted = dc.encrypt("Top Secret", combined)
decrypted = dc.decrypt(encrypted, combined)
```

---

## 🪔 Devanagari Encoding (Optional Layer)

Use this for culturally authentic encrypted outputs.

```python
# Encode encrypted output
devnagari = dc.devanagari_encode(encrypted)
print("Devanagari Encoded:", devnagari)

# Decode then decrypt
decoded = dc.devanagari_decode(devnagari)
plain = dc.decrypt(decoded, combined)
print("Decrypted:", plain)
```

---

## 🔐 Working with Secrets

Generate a secure server token:

```python
token = dc.generate_server_token()
print("Token:", token)
```

---

## 🔑 Combined Utility Wrappers

DevCrypt provides simplified encrypt() and decrypt() wrapper functions:

```python
from devcrypt import encrypt, decrypt

ciphertext, token = encrypt("Encrypt this!", "MyPassword")
plaintext = decrypt(ciphertext, "MyPassword", token)
```

---

## 💡 Common Use Cases

### 1. Secure Configuration

```python
config_data = '{"api_key": "super-secret", "host": "localhost"}'
ciphertext, token = encrypt(config_data, "configPass")
# Save ciphertext and token
```

### 2. Password Protection

```python
pw = "myRealPassword!"
encrypted_pw, token = encrypt(pw, "masterKey")
# Verify later
assert decrypt(encrypted_pw, "masterKey", token) == pw
```

### 3. Devanagari Encryption (for India-specific data)

```python
text = "सुरक्षित संदेश"
ciphertext, token = encrypt(text, "पासवर्ड")
encoded = dc.devanagari_encode(ciphertext)
decoded = dc.devanagari_decode(encoded)
plain = decrypt(decoded, "पासवर्ड", token)
```

---

## ⚠️ Error Handling

```python
try:
    decrypted = decrypt(ciphertext, "wrongpassword", token)
except ValueError as e:
    print("Decryption failed:", e)
```

---

## 🛡️ Best Practices

- Always use strong passwords
- Store tokens securely (never hardcode)
- Don’t reuse tokens for multiple users
- Always encode/decode properly if using Devanagari
- Catch and handle all exceptions
- Never expose internal keys, salt, IV in plaintext

---

## 🔧 Next Steps

- Check out the full documentation
- Browse more examples
- Read the DevCrypt Security Analysis
- Report bugs on GitHub

---

## 📜 License

© 2025 Atharva Panchal and Mohit Chadhuari.  
Licensed under the MIT License with Attribution. See LICENSE for more details.
