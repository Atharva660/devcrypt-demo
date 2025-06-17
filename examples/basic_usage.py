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

from devcrypt import DevCrypt, DevCryptError, InvalidKeyError
import sys

def basic_text_encryption():
    """Demonstrate basic text encryption and decryption"""
    print("=== Basic Text Encryption ===")
    
    # Initialize DevCrypt
    dc = DevCrypt()
    
    # Sample message
    original_message = "Hello, this is a secret message!"
    print(f"Original message: {original_message}")
    
    # Encrypt using default method (Fernet)
    encrypted = dc.encrypt(original_message)
    print(f"Encrypted (Fernet): {encrypted}")
    
    # Decrypt the message
    decrypted = dc.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")
    
    # Verify the decryption worked
    assert original_message == decrypted, "Decryption failed!"
    print("✅ Basic encryption/decryption successful!\n")

def multiple_encryption_methods():
    """Demonstrate different encryption methods"""
    print("=== Multiple Encryption Methods ===")
    
    dc = DevCrypt()
    message = "Testing different encryption methods"
    
    methods = ["fernet", "aes"]
    
    for method in methods:
        try:
            print(f"\nTesting {method.upper()} encryption:")
            encrypted = dc.encrypt(message, method=method)
            decrypted = dc.decrypt(encrypted, method=method)
            
            print(f"  Original: {message}")
            print(f"  Encrypted: {encrypted[:50]}..." if len(str(encrypted)) > 50 else f"  Encrypted: {encrypted}")
            print(f"  Decrypted: {decrypted}")
            
            assert message == decrypted, f"{method} encryption failed!"
            print(f"  ✅ {method.upper()} encryption successful!")
            
        except Exception as e:
            print(f"  ❌ {method.upper()} encryption failed: {e}")

def key_management_demo():
    """Demonstrate key generation and management"""
    print("\n=== Key Management ===")
    
    dc = DevCrypt()
    
    # Generate different types of keys
    print("Generating keys...")
    
    # Fernet key
    fernet_key = dc.generate_key("fernet")
    print(f"Fernet key generated: {fernet_key[:20]}...")
    
    # AES key
    aes_key = dc.generate_key("aes")
    print(f"AES key generated: {aes_key[:20]}...")
    
    # Use custom key for encryption
    print("\nUsing custom key for encryption:")
    custom_dc = DevCrypt(key=fernet_key)
    message = "Message with custom key"
    encrypted = custom_dc.encrypt(message)
    decrypted = custom_dc.decrypt(encrypted)
    
    print(f"Message: {message}")
    print(f"Decrypted: {decrypted}")
    assert message == decrypted, "Custom key encryption failed!"
    print("✅ Custom key encryption successful!")

def error_handling_demo():
    """Demonstrate proper error handling"""
    print("\n=== Error Handling ===")
    
    dc = DevCrypt()
    
    # Test invalid decryption
    print("Testing error scenarios...")
    
    try:
        # Try to decrypt random data
        dc.decrypt("invalid_encrypted_data")
    except DevCryptError as e:
        print(f"✅ Caught expected DecryptionError: {e}")
    
    try:
        # Try unsupported method
        dc.encrypt("test", method="nonexistent_method")
    except Exception as e:
        print(f"✅ Caught expected UnsupportedMethodError: {e}")
    
    try:
        # Try with invalid key
        dc.decrypt("test", key="invalid_key")
    except Exception as e:
        print(f"✅ Caught expected InvalidKeyError: {e}")

def performance_comparison():
    """Compare performance of different methods"""
    print("\n=== Performance Comparison ===")
    
    import time
    
    dc = DevCrypt()
    test_data = "This is a test message for performance comparison." * 100  # Larger message
    
    methods = ["fernet", "aes"]
    
    print(f"Testing with message of {len(test_data)} characters")
    
    for method in methods:
        try:
            # Measure encryption time
            start_time = time.time()
            encrypted = dc.encrypt(test_data, method=method)
            encrypt_time = time.time() - start_time
            
            # Measure decryption time
            start_time = time.time()
            decrypted = dc.decrypt(encrypted, method=method)
            decrypt_time = time.time() - start_time
            
            print(f"{method.upper()}:")
            print(f"  Encryption time: {encrypt_time:.4f} seconds")
            print(f"  Decryption time: {decrypt_time:.4f} seconds")
            print(f"  Total time: {encrypt_time + decrypt_time:.4f} seconds")
            
            # Verify correctness
            assert test_data == decrypted, f"{method} performance test failed!"
            print(f"  ✅ Verification successful")
            
        except Exception as e:
            print(f"  ❌ {method} performance test failed: {e}")
        
        print()

def interactive_demo():
    """Interactive demo for user input"""
    print("\n=== Interactive Demo ===")
    
    dc = DevCrypt()
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        try:
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == "1":
                message = input("Enter message to encrypt: ")
                method = input("Enter method (fernet/aes) or press Enter for default: ").strip() or "fernet"
                
                try:
                    encrypted = dc.encrypt(message, method=method)
                    print(f"Encrypted message: {encrypted}")
                except Exception as e:
                    print(f"Encryption failed: {e}")
            
            elif choice == "2":
                encrypted_input = input("Enter encrypted message: ")
                method = input("Enter method (fernet/aes) or press Enter for default: ").strip() or "fernet"
                
                try:
                    decrypted = dc.decrypt(encrypted_input, method=method)
                    print(f"Decrypted message: {decrypted}")
                except Exception as e:
                    print(f"Decryption failed: {e}")
            
            elif choice == "3":
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    print("DevCrypt Basic Usage Examples")
    print("=" * 40)
    
    try:
        # Run all demos
        basic_text_encryption()
        multiple_encryption_methods()
        key_management_demo()
        error_handling_demo()
        performance_comparison()
        
        # Ask if user wants interactive demo
        if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
            interactive_demo()
        else:
            print("Run with --interactive flag for interactive demo")
        
        print("\n🎉 All basic usage examples completed successfully!")
        
    except KeyboardInterrupt:
        print("\n\nExiting...")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)