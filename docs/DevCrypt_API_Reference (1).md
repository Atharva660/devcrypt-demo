# 📘 DevCrypt API Reference

Complete reference for all DevCrypt classes and functions.

---

## 🔐 DevCrypt Class

The main class for encryption, decryption, and Devanagari encoding operations.

---

## 🛠️ Constructor

```python
DevCrypt()
```

No arguments required. Uses secure defaults for AES-256-CBC encryption with Argon2id-based key derivation and HMAC-SHA256 integrity.

---

## 🔑 Core Methods

### 🔒 encrypt()

Encrypts plaintext using AES-256-CBC and authenticates with HMAC-SHA256.

```python
encrypt(plaintext: str, combined_secret: str) -> str
```

* `plaintext`: Data to encrypt
* `combined_secret`: A secure string formed from user password and server token
* Returns: Base64-encoded encrypted string (includes salt, IV, ciphertext, HMAC)

---

### 🔓 decrypt()

Decrypts a base64-encoded encrypted string.

```python
decrypt(b64_data: str, combined_secret: str) -> str
```

* `b64_data`: Encrypted base64 string
* `combined_secret`: Same password + token combination used during encryption
* Returns: Original plaintext if HMAC is verified, otherwise raises error

---

## 🧠 Key Derivation

### 🧂 derive_key()

Derives a strong encryption key using Argon2id.

```python
derive_key(password: str, salt: bytes) -> bytes
```

* `password`: Combined user password + token
* `salt`: Random 16-byte salt
* Returns: 32-byte AES key

---

## 🔐 HMAC for Integrity

Uses SHA-256 to prevent tampering.

### 📎 verify_hmac()

```python
verify_hmac(ciphertext: bytes, iv: bytes, salt: bytes, hmac_value: bytes, key: bytes) -> bool
```

Raises `InvalidKeyError` if authentication fails.

---

## 🧮 Utility Functions

### 🔗 combine_factors()

Combine user password and server-generated token.

```python
combine_factors(user_password: str, server_token: str) -> str
```

---

### 🔐 generate_server_token()

Secure random token generator.

```python
generate_server_token(length=32) -> str
```

---

## 🇮🇳 Devanagari Encoding

Unique textual encryption layer using Indian script.

### 📜 devanagari_encode()

```python
devanagari_encode(text: str) -> str
```

Encodes Latin text to Devanagari symbols.

---

### 🔁 devanagari_decode()

```python
devanagari_decode(encoded_text: str) -> str
```

Restores original Latin text from Devanagari symbols.

---

## 🚀 Convenience API

### encrypt()

Encrypt using password + token.

```python
encrypt(plaintext: str, user_password: str, server_token: str = None) -> Tuple[str, str]
```

* Returns: Tuple of `(encrypted_data, generated_token)`

---

### decrypt()

```python
decrypt(b64_data: str, user_password: str, server_token: str) -> str
```

* Returns: Original string if password/token are correct

---

## 📦 Properties

### ✅ supported_methods

```python
['aes-256-cbc', 'devanagari']
```

---

### 🧾 version

```python
'2.0.0'
```

---

## ⚠️ Exceptions

### DevCryptError

Raised on generic cryptographic issues.

---

### InvalidKeyError

Raised when HMAC verification fails or key is incorrect.

---

## 💡 Example Usage

```python
from devcrypt import encrypt, decrypt

# Encrypt a message
encrypted, token = encrypt("Secret data", "mypassword")
print("Encrypted:", encrypted)
print("Token:", token)

# Decrypt the message
decrypted = decrypt(encrypted, "mypassword", token)
print("Decrypted:", decrypted)
```

---

© 2025 Atharva Panchal and Mohit Chadhuari.
Licensed under the MIT License with Attribution. See [LICENSE](../LICENSE) for more details.