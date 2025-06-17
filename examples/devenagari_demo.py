#!/usr/bin/env python3
# DevCrypt Examples
# (c) 2025 Atharva Panchal and Mohit Chadhuari
# Licensed under the MIT License with Attribution
# See LICENSE in the repository root for more info


"""
DevCrypt Devanagari Script Demo

This script demonstrates DevCrypt's unique Devanagari script encoding feature:
- Basic Devanagari encoding/decoding
- Different complexity levels
- Cultural text preservation
- Unicode handling
- Visual examples
"""

from devcrypt import DevCrypt, DevCryptError
import sys

def print_separator(title):
    """Print a formatted separator"""
    print("\n" + "=" * 50)
    print(f" {title} ")
    print("=" * 50)

def basic_devanagari_demo():
    """Demonstrate basic Devanagari encoding and decoding"""
    print_separator("Basic Devanagari Encoding")
    
    dc = DevCrypt()
    
    # Sample messages
    messages = [
        "Hello World",
        "This is a secret message",
        "DevCrypt is awesome!",
        "नमस्ते - Mixed text example"
    ]
    
    for message in messages:
        print(f"\nOriginal: {message}")
        
        try:
            # Encode to Devanagari
            encoded = dc.devanagari_encode(message)
            print(f"Encoded:  {encoded}")
            
            # Decode back to original
            decoded = dc.devanagari_decode(encoded)
            print(f"Decoded:  {decoded}")
            
            # Verify accuracy
            assert message == decoded, "Encoding/decoding mismatch!"
            print("✅ Success!")
            
        except Exception as e:
            print(f"❌ Error: {e}")

def complexity_levels_demo():
    """Demonstrate different complexity levels"""
    print_separator("Complexity Levels")
    
    dc = DevCrypt()
    message = "Secret message for complexity testing"
    
    complexities = ["simple", "medium", "complex"]
    
    print(f"Original message: {message}")
    
    for complexity in complexities:
        try:
            print(f"\n--- {complexity.upper()} Complexity ---")
            
            # Encode with specific complexity
            encoded = dc.devanagari_encode(message, complexity=complexity)
            print(f"Encoded ({complexity}): {encoded}")
            
            # Decode back
            decoded = dc.devanagari_decode(encoded, complexity=complexity)
            print(f"Decoded: {decoded}")
            
            # Verify
            assert message == decoded, f"{complexity} complexity failed!"
            print(f"✅ {complexity.capitalize()} complexity successful!")
            
        except Exception as e:
            print(f"❌ {complexity} complexity failed: {e}")

def cultural_text_demo():
    """Demonstrate encoding of cultural and multilingual text"""
    print_separator("Cultural Text Examples")
    
    dc = DevCrypt()
    
    # Various cultural texts
    cultural_texts = [
        "नमस्ते दुनिया",  # Hindi greeting
        "Sanskrit श्लोक example",  # Mixed script
        "Prayer: ॐ मणि पद्मे हूँ",  # Religious text
        "Mathematical: २ + २ = ४",  # Devanagari numerals
        "Modern: DevCrypt + देवनागरी = 💫"  # Tech + culture
    ]
    
    for text in cultural_texts:
        print(f"\nOriginal: {text}")
        
        try:
            encoded = dc.devanagari_encode(text)
            decoded = dc.devanagari_decode(encoded)
            
            print(f"Encoded:  {encoded}")
            print(f"Decoded:  {decoded}")
            
            assert text == decoded, "Cultural text encoding failed!"
            print("✅ Cultural text preserved successfully!")
            
        except Exception as e:
            print(f"❌ Error with cultural text: {e}")

def visual_comparison_demo():
    """Visual comparison between regular encryption and Devanagari encoding"""
    print_separator("Visual Comparison")
    
    dc = DevCrypt()
    message = "This is a confidential document"
    
    print(f"Original Message: {message}")
    print(f"Length: {len(message)} characters\n")
    
    # Regular encryption
    try:
        regular_encrypted = dc.encrypt(message, method="fernet")
        print("--- Regular Encryption ---")
        print(f"Encrypted: {regular_encrypted}")
        print(f"Type: Binary/Base64 encoded")
        print(f"Human readable: No")
        
        # Devanagari encoding
        devanagari_encoded = dc.devanagari_encode(message)
        print("\n--- Devanagari Encoding ---")
        print(f"Encoded: {devanagari_encoded}")
        print(f"Type: Unicode Devanagari script")
        print(f"Human readable: Yes (appears as text)")
        print(f"Cultural significance: High")
        
        # Verify both work
        regular_decrypted = dc.decrypt(regular_encrypted, method="fernet")
        devanagari_decoded = dc.devanagari_decode(devanagari_encoded)
        
        assert message == regular_decrypted == devanagari_decoded
        print("\n✅ Both methods work correctly!")
        
    except Exception as e:
        print(f"❌ Comparison failed: {e}")

def unicode_handling_demo():
    """Demonstrate Unicode and special character handling"""
    print_separator("Unicode Handling")
    
    dc = DevCrypt()
    
    # Various Unicode texts
    unicode_texts = [
        "Emoji test: 🔐🌟💻",
        "Symbols: ∑∆∞±≠≤≥",
        "Accented: café, naïve, résumé",
        "Mixed: Hello नमस्ते 你好 مرحبا",
        "Special chars: @#$%^&*()_+-=[]{}|;':\",./<>?"
    ]
    
    for text in unicode_texts:
        print(f"\nTesting: {text}")
        
        try:
            encoded = dc.devanagari_encode(text)
            decoded = dc.devanagari_decode(encoded)
            
            print(f"Encoded:  {encoded}")
            print(f"Success:  {text == decoded}")
            
            if text != decoded:
                print(f"Expected: {text}")
                print(f"Got:      {decoded}")
            
        except Exception as e:
            print(f"Error: {e}")

def performance_analysis():
    """Analyze performance of Devanagari encoding vs regular encryption"""
    print_separator("Performance Analysis")
    
    import time
    
    dc = DevCrypt()
    
    # Test with different message sizes
    test_sizes = [10, 100, 1000, 5000]
    
    for size in test_sizes:
        message = "A" * size
        print(f"\n--- Testing with {size} characters ---")
        
        # Devanagari encoding performance
        start_time = time.time()
        encoded = dc.devanagari_encode(message)
        encode_time = time.time() - start_time
        
        start_time = time.time()
        decoded = dc.devanagari_decode(encoded)
        decode_time = time.time() - start_time
        
        print(f"Devanagari Encoding: {encode_time:.4f}s")
        print(f"Devanagari Decoding: {decode_time:.4f}s")
        print(f"Total Devanagari:    {encode_time + decode_time:.4f}s")
        
        # Regular encryption performance
        start_time = time.time()
        encrypted = dc.encrypt(message, method="fernet")
        encrypt_time = time.time() - start_time
        
        start_time = time.time()
        decrypted = dc.decrypt(encrypted, method="fernet")
        decrypt_time = time.time() - start_time
        
        print(f"Regular Encryption:  {encrypt_time:.4f}s")
        print(f"Regular Decryption:  {decrypt_time:.4f}s")
        print(f"Total Regular:       {encrypt_time + decrypt_time:.4f}s")
        
        # Verify correctness
        assert message == decoded == decrypted
        print("✅ Both methods verified correct")

def interactive_devanagari():
    """Interactive Devanagari encoding session"""
    print_separator("Interactive Devanagari Session")
    
    dc = DevCrypt()
    
    print("Welcome to interactive Devanagari encoding!")
    print("Enter messages to encode/decode, or 'quit' to exit.\n")
    
    while True:
        try:
            print("\nOptions:")
            print("1. Encode message to Devanagari")
            print("2. Decode Devanagari message")
            print("3. Quit")
            
            choice = input("\nSelect option (1-3): ").strip()
            
            if choice == "1":
                message = input("Enter message to encode: ")
                complexity = input("Complexity (simple/medium/complex) [medium]: ").strip() or "medium"
                
                try:
                    encoded = dc.devanagari_encode(message, complexity=complexity)
                    print(f"\nEncoded message: {encoded}")
                    print("Copy this encoded message to decode later!")
                except Exception as e:
                    print(f"Encoding failed: {e}")
            
            elif choice == "2":
                encoded_message = input("Enter Devanagari encoded message: ")
                complexity = input("Complexity used (simple/medium/complex) [medium]: ").strip() or "medium"
                
                try:
                    decoded = dc.devanagari_decode(encoded_message, complexity=complexity)
                    print(f"\nDecoded message: {decoded}")
                except Exception as e:
                    print(f"Decoding failed: {e}")
            
            elif choice == "3":
                print("Goodbye! धन्यवाद (Thank you)!")
                break
            
            else:
                print("Invalid choice. Please try again.")
        
        except KeyboardInterrupt:
            print("\nGoodbye! धन्यवाद (Thank you)!")
            break
        except EOFError:
            print("\nGoodbye! धन्यवाद (Thank you)!")
            break

if __name__ == "__main__":
    print("DevCrypt Devanagari Script Demo")
    print("Preserving culture through encryption 🕉️")
    
    try:
        # Run all demos
        basic_devanagari_demo()
        complexity_levels_demo()
        cultural_text_demo()
        visual_comparison_demo()
        unicode_handling_demo()
        performance_analysis()
        
        # Interactive session
        if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
            interactive_devanagari()
        else:
            print("\n" + "=" * 50)
            print("Run with --interactive flag for hands-on experience!")
        
        print("\n🕉️ Devanagari demo completed successfully!")
        print("Culture and technology united through DevCrypt!")
        
    except KeyboardInterrupt:
        print("\n\nनमस्ते! (Goodbye!)")
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        sys.exit(1)
    