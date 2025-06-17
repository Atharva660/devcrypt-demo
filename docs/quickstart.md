# Quick Start Guide
Get up and running with DevCrypt in minutes!

Your First Encryption
python
from devcrypt import DevCrypt

# Create a DevCrypt instance
dc = DevCrypt()

# Encrypt a message
message = "Hello, World!"
encrypted = dc.encrypt(message)
print(f"Encrypted: {encrypted}")

# Decrypt the message
decrypted = dc.decrypt(encrypted)
print(f"Decrypted: {decrypted}")
Basic Concepts
1. Initialization
python
from devcrypt import DevCrypt

# Default initialization
dc = DevCrypt()

# With custom key
dc = DevCrypt(key="your-secret-key")

# With specific algorithm
dc = DevCrypt(default_method="aes")
2. Text Encryption
python
# Using default method (Fernet)
encrypted = dc.encrypt("Secret message")

# Using specific method
encrypted_aes = dc.encrypt("Secret message", method="aes")
encrypted_rsa = dc.encrypt("Secret message", method="rsa")
3. File Encryption
python
# Encrypt a file
dc.encrypt_file("input.txt", "output.enc")

# Decrypt a file
dc.decrypt_file("output.enc", "restored.txt")
Devanagari Encoding
DevCrypt's unique feature - encoding text using Devanagari script:

python
# Encode text to Devanagari
text = "This is a secret message"
encoded = dc.devanagari_encode(text)
print(f"Encoded: {encoded}")  # देवनागरी में

# Decode back to original
decoded = dc.devanagari_decode(encoded)
print(f"Decoded: {decoded}")
Working with Keys
Generate New Keys
python
# Generate Fernet key
fernet_key = dc.generate_key("fernet")

# Generate RSA key pair
public_key, private_key = dc.generate_key_pair("rsa")
Save/Load Keys
python
# Save key to file
dc.save_key(key, "mykey.key")

# Load key from file
loaded_key = dc.load_key("mykey.key")
Common Use Cases
1. Secure Configuration
python
# Encrypt sensitive config
config = {
    "database_url": "postgresql://user:pass@localhost/db",
    "api_key": "secret-api-key"
}

encrypted_config = dc.encrypt(str(config))
# Save encrypted_config to file
2. Password Protection
python
# Encrypt passwords
password = "super_secret_password"
encrypted_password = dc.encrypt(password)

# Later verify
decrypted_password = dc.decrypt(encrypted_password)
is_valid = password == decrypted_password
3. File Backup
python
import os

# Encrypt all files in a directory
for filename in os.listdir("sensitive_files/"):
    if filename.endswith(".txt"):
        dc.encrypt_file(
            f"sensitive_files/{filename}",
            f"encrypted_backup/{filename}.enc"
        )
Command Line Usage
DevCrypt also provides a CLI interface:

bash
# Encrypt a file
devcrypt encrypt input.txt -o output.enc

# Decrypt a file
devcrypt decrypt output.enc -o restored.txt

# Generate a key
devcrypt keygen -t fernet -o mykey.key

# Devanagari encoding
devcrypt encode "Hello World" --devanagari
Error Handling
python
try:
    encrypted = dc.encrypt("message")
    decrypted = dc.decrypt(encrypted)
except DevCryptError as e:
    print(f"Encryption error: {e}")
except InvalidKeyError as e:
    print(f"Invalid key: {e}")
Best Practices
Always use unique keys for different applications
Store keys securely - never hardcode them
Use appropriate methods - RSA for small data, AES for large data
Handle errors gracefully with try-catch blocks
Test your encryption/decryption before deploying
Next Steps
Explore more examples
Read the complete API reference
Check out the example scripts
Need Help?
Check the API Reference for detailed function documentation
Look at examples for real-world usage
Open an issue on GitHub for bugs or questions

© 2025 Atharva Panchal and Mohit Chadhuari.  
Licensed under the MIT License with Attribution. See [LICENSE](../LICENSE) for more details
