# 📘 DevCrypt API Reference

Complete reference for all DevCrypt classes and functions.

---

## 🔐 DevCrypt Class

The main class for encryption, decryption, and Devanagari encoding operations.

### 🛠️ Constructor

```python
DevCrypt()
No arguments required. Uses secure defaults for AES-256 encryption with Argon2id-based key derivation.

🔑 Core Methods
🔒 encrypt()
Encrypts text using AES-256-CBC and HMAC-SHA256.


encrypt(plaintext: str, combined_secret: str) -> str
plaintext: Data to encrypt (str)

combined_secret: Result of user_password + server_token

Returns: Encrypted string in base64

🔓 decrypt()
Decrypts previously encrypted base64-encoded text.


decrypt(b64_data: str, combined_secret: str) -> str
b64_data: Encrypted base64 string

combined_secret: Result of user_password + server_token

Returns: Decrypted original string

🧠 Key Derivation
🧂 derive_key()
Uses Argon2id to derive a 256-bit key.


derive_key(password: str, salt: bytes) -> bytes
password: Combined user password and server token

salt: Random 16-byte salt

Returns: 32-byte encryption key

🧮 Utility Functions
🔗 combine_factors()

combine_factors(user_password: str, server_token: str) -> str
Combines user password and server-generated token.

🔐 generate_server_token()
Generates a secure random server token.


generate_server_token(length=32) -> str
length: Length of token (default: 32)

Returns: Secure random string

🇮🇳 Devanagari Encoding Methods
📜 devanagari_encode()
Encodes ASCII text into Devanagari representation.


devanagari_encode(text: str) -> str
text: Text to encode

Returns: Devanagari-encoded string

🔁 devanagari_decode()
Decodes Devanagari back to ASCII.


devanagari_decode(encoded_text: str) -> str
encoded_text: Devanagari string

Returns: Decoded original string

🧪 Convenience API
encrypt()
Encrypt using user_password + server_token.


encrypt(plaintext: str, user_password: str, server_token: str = None) -> Tuple[str, str]
Returns (encrypted_data, token)

decrypt()

decrypt(b64_data: str, user_password: str, server_token: str) -> str
Returns original plaintext.

📦 Properties
✅ supported_methods

['aes-256-cbc', 'devanagari']
'2.0.0'
⚠️ Exceptions
DevCryptError
Generic error

InvalidKeyError
Raised for HMAC or decryption issues

💡 Example Usage

from devcrypt import encrypt, decrypt

# Encrypt a message
encrypted, token = encrypt("Secret data", "mypassword")
print("Encrypted:", encrypted)
print("Token:", token)

# Decrypt it back
decrypted = decrypt(encrypted, "mypassword", token)
print("Decrypted:", decrypted)
© 2025 Atharva Panchal and Mohit Chadhuari.
Licensed under the MIT License with Attribution. See LICENSE for more details.