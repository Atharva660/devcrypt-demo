
# API Reference
Complete reference for all DevCrypt classes and functions.

DevCrypt Class
The main class for encryption and decryption operations.

Constructor
python
DevCrypt(key=None, default_method="fernet")
Parameters:

key (str, optional): Default encryption key. If None, a key will be generated.
default_method (str): Default encryption method. Options: "fernet", "aes", "rsa", "devanagari"
Example:

python
dc = DevCrypt(key="my-secret-key", default_method="aes")
Core Methods
encrypt()
Encrypts text or bytes using the specified method.

python
encrypt(data, method=None, key=None)
Parameters:

data (str or bytes): Data to encrypt
method (str, optional): Encryption method to use
key (str, optional): Specific key for this operation
Returns: Encrypted data as bytes or encoded string

Example:

python
encrypted = dc.encrypt("Hello World", method="aes")
decrypt()
Decrypts previously encrypted data.

python
decrypt(encrypted_data, method=None, key=None)
Parameters:

encrypted_data (bytes or str): Data to decrypt
method (str, optional): Decryption method to use
key (str, optional): Specific key for this operation
Returns: Decrypted data as string

Example:

python
decrypted = dc.decrypt(encrypted_data, method="aes")
File Operations
encrypt_file()
Encrypts a file and saves it to a new location.

python
encrypt_file(input_path, output_path, method=None, key=None)
Parameters:

input_path (str): Path to the file to encrypt
output_path (str): Path where encrypted file will be saved
method (str, optional): Encryption method
key (str, optional): Encryption key
Example:

python
dc.encrypt_file("document.pdf", "document.enc")
decrypt_file()
Decrypts a file and saves it to a new location.

python
decrypt_file(input_path, output_path, method=None, key=None)
Parameters:

input_path (str): Path to the encrypted file
output_path (str): Path where decrypted file will be saved
method (str, optional): Decryption method
key (str, optional): Decryption key
Example:

python
dc.decrypt_file("document.enc", "document_restored.pdf")
Devanagari Methods
devanagari_encode()
Encodes text using Devanagari script-based encoding.

python
devanagari_encode(text, complexity="medium")
Parameters:

text (str): Text to encode
complexity (str): Encoding complexity. Options: "simple", "medium", "complex"
Returns: Encoded text in Devanagari script

Example:

python
encoded = dc.devanagari_encode("Secret message")
devanagari_decode()
Decodes Devanagari-encoded text back to original.

python
devanagari_decode(encoded_text, complexity="medium")
Parameters:

encoded_text (str): Devanagari-encoded text
complexity (str): Decoding complexity (must match encoding)
Returns: Original text as string

Example:

python
decoded = dc.devanagari_decode(encoded_text)
Key Management
generate_key()
Generates a new encryption key for the specified method.

python
generate_key(method="fernet")
Parameters:

method (str): Encryption method. Options: "fernet", "aes", "rsa"
Returns: Generated key as bytes or string

Example:

python
key = dc.generate_key("fernet")
generate_key_pair()
Generates a public/private key pair for asymmetric encryption.

python
generate_key_pair(method="rsa", key_size=2048)
Parameters:

method (str): Asymmetric method. Currently supports "rsa"
key_size (int): Key size in bits
Returns: Tuple of (public_key, private_key)

Example:

python
public_key, private_key = dc.generate_key_pair("rsa", 2048)
save_key()
Saves a key to a file.

python
save_key(key, filepath, password=None)
Parameters:

key (bytes or str): Key to save
filepath (str): Path where key will be saved
password (str, optional): Password to protect the key file
Example:

python
dc.save_key(key, "mykey.key", password="keypass")
load_key()
Loads a key from a file.

python
load_key(filepath, password=None)
Parameters:

filepath (str): Path to the key file
password (str, optional): Password to unlock the key file
Returns: Loaded key

Example:

python
key = dc.load_key("mykey.key", password="keypass")
Utility Methods
hash_data()
Creates a hash of the input data.

python
hash_data(data, algorithm="sha256")
Parameters:

data (str or bytes): Data to hash
algorithm (str): Hash algorithm. Options: "md5", "sha1", "sha256", "sha512"
Returns: Hash as hexadecimal string

Example:

python
hash_value = dc.hash_data("Hello World", "sha256")
verify_hash()
Verifies if data matches a given hash.

python
verify_hash(data, hash_value, algorithm="sha256")
Parameters:

data (str or bytes): Original data
hash_value (str): Hash to verify against
algorithm (str): Hash algorithm used
Returns: Boolean indicating if hash matches

Example:

python
is_valid = dc.verify_hash("Hello World", hash_value, "sha256")
Properties
supported_methods
List of supported encryption methods.

python
print(dc.supported_methods)
# Output: ['fernet', 'aes', 'rsa', 'devanagari']
version
Current version of DevCrypt.

python
print(dc.version)
# Output: '1.0.0'
Exceptions
DevCryptError
Base exception for all DevCrypt errors.

python
try:
    dc.encrypt("data")
except DevCryptError as e:
    print(f"DevCrypt error: {e}")
InvalidKeyError
Raised when an invalid key is provided.

python
try:
    dc.decrypt(data, key="invalid")
except InvalidKeyError as e:
    print(f"Invalid key: {e}")
UnsupportedMethodError
Raised when an unsupported encryption method is specified.

python
try:
    dc.encrypt("data", method="unknown")
except UnsupportedMethodError as e:
    print(f"Unsupported method: {e}")
FileNotFoundError
Raised when a specified file cannot be found.

python
try:
    dc.encrypt_file("nonexistent.txt", "output.enc")
except FileNotFoundError as e:
    print(f"File not found: {e}")
Constants
python
from devcrypt.constants import (
    DEFAULT_KEY_SIZE,      # 2048
    MAX_FILE_SIZE,         # 100MB
    SUPPORTED_ALGORITHMS,  # ['fernet', 'aes', 'rsa', 'devanagari']
    DEVANAGARI_CHARSET    # Devanagari character set
)
Examples
Complete Example
python
from devcrypt import DevCrypt, DevCryptError

try:
    # Initialize
    dc = DevCrypt()
    
    # Text encryption
    message = "Confidential information"
    encrypted = dc.encrypt(message, method="aes")
    decrypted = dc.decrypt(encrypted, method="aes")
    
    # File encryption
    dc.encrypt_file("secret.txt", "secret.enc")
    dc.decrypt_file("secret.enc", "secret_restored.txt")
    
    # Devanagari encoding
    encoded = dc.devanagari_encode("Hidden message")
    decoded = dc.devanagari_decode(encoded)
    
    # Key management
    key = dc.generate_key("fernet")
    dc.save_key(key, "backup.key")
    
    print("All operations completed successfully!")
    
except DevCryptError as e:
    print(f"Error: {e}")
This completes the API reference. For more examples and use cases, see the examples directory.

© 2025 Atharva Panchal and Mohit Chadhuari.  
Licensed under the MIT License with Attribution. See [LICENSE](../LICENSE) for more details