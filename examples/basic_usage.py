#!/usr/bin/env python3
# DevCrypt Examples
# (c) 2025 Atharva Panchal and Mohit Chadhuari
# Licensed under the MIT License with Attribution
# See LICENSE in the repository root for more info

"""
DevCrypt Basic Usage Examples

This script demonstrates the basic functionality of DevCrypt including:
- Text encryption and decryption
- Different encryption methods
- Key generation and management
- Error handling
"""

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


### Step 2: Decrypting Your Message

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