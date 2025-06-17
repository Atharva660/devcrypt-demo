#!/usr/bin/env python3
# DevCrypt Examples
# (c) 2025 Atharva Panchal and Mohit Chadhuari
# Licensed under the MIT License with Attribution
# See LICENSE in the repository root for more info

"""
DevCrypt File Encryption Examples

This script demonstrates file encryption and decryption capabilities:
- Single file encryption/decryption
- Batch file processing
- Directory encryption
- Different file types
- Progress tracking
- Secure file deletion
"""

import os
import sys
import time
import shutil
from pathlib import Path
from devcrypt import DevCrypt, DevCryptError

def create_sample_files():
    """Create sample files for demonstration"""
    print("Creating sample files for demonstration...")
    
    # Create a sample directory
    sample_dir = Path("sample_files")
    sample_dir.mkdir(exist_ok=True)
    
    # Sample text file
    with open(sample_dir / "document.txt", "w", encoding="utf-8") as f:
        f.write("""DevCrypt File Encryption Demo
        
This is a sample text document containing sensitive information:
- Personal details
- Financial records
- Confidential business data
- Important passwords and keys

This file will be encrypted to protect its contents.
""")
    
    # Sample configuration file
    with open(sample_dir / "config.json", "w", encoding="utf-8") as f:
        f.write("""{
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": "admin",
        "password": "super_secret_password"
    },
    "api_keys": {
        "stripe": "sk_test_secret_key_here",
        "sendgrid": "SG.secret_api_key_here"
    },
    "encryption": {
        "method": "aes",
        "key_rotation": true
    }
}""")
    
    # Sample binary file (simulate an image)
    with open(sample_dir / "image.bin", "wb") as f:
        # Create some binary data
        binary_data = bytes(range(256)) * 100  # 25.6 KB of binary data
        f.write(binary_data)
    
    # Sample CSV file
    with open(sample_dir / "data.csv", "w", encoding="utf-8") as f:
        f.write("""Name,Email,Phone,SSN
John Doe,john@example.com,123-456-7890,123-45-6789
Jane Smith,jane@example.com,098-765-4321,987-65-4321
Bob Johnson,bob@example.com,555-123-4567,456-78-9012
""")
    
    print(f"✅ Sample files created in {sample_dir}/")
    return sample_dir

def single_file_encryption():
    """Demonstrate single file encryption and decryption"""
    print("\n" + "="*50)
    print(" Single File Encryption Demo ")
    print("="*50)
    
    dc = DevCrypt()
    sample_dir = Path("sample_files")
    
    # Encrypt the text document
    input_file = sample_dir / "document.txt"
    encrypted_file = sample_dir / "document.txt.enc"
    decrypted_file = sample_dir / "document_restored.txt"
    
    print(f"Encrypting: {input_file}")
    
    try:
        # Check original file size
        original_size = input_file.stat().st_size
        print(f"Original file size: {original_size} bytes")
        
        # Encrypt the file
        start_time = time.time()
        dc.encrypt_file(str(input_file), str(encrypted_file))
        encrypt_time = time.time() - start_time
        
        encrypted_size = encrypted_file.stat().st_size
        print(f"Encrypted file size: {encrypted_size} bytes")
        print(f"Encryption time: {encrypt_time:.4f} seconds")
        print(f"✅ File encrypted successfully: {encrypted_file}")
        
        # Decrypt the file
        print(f"\nDecrypting: {encrypted_file}")
        start_time = time.time()
        dc.decrypt_file(str(encrypted_file), str(decrypted_file))
        decrypt_time = time.time() - start_time
        
        decrypted_size = decrypted_file.stat().st_size
        print(f"Decrypted file size: {decrypted_size} bytes")
        print(f"Decryption time: {decrypt_time:.4f} seconds")
        print(f"✅ File decrypted successfully: {decrypted_file}")
        
        # Verify file integrity
        with open(input_file, 'r') as f1, open(decrypted_file, 'r') as f2:
            original_content = f1.read()
            decrypted_content = f2.read()
            
            if original_content == decrypted_content:
                print("✅ File integrity verified - contents match!")
            else:
                print("❌ File integrity check failed!")
        
    except Exception as e:
        print(f"❌ Single file encryption failed: {e}")

def batch_file_encryption():
    """Demonstrate batch encryption of multiple files"""
    print("\n" + "="*50)
    print(" Batch File Encryption Demo ")
    print("="*50)
    
    dc = DevCrypt()
    sample_dir = Path("sample_files")
    encrypted_dir = Path("encrypted_files")
    encrypted_dir.mkdir(exist_ok=True)
    
    # Get all files to encrypt
    files_to_encrypt = [f for f in sample_dir.iterdir() if f.is_file() and not f.name.endswith('.enc')]
    
    print(f"Found {len(files_to_encrypt)} files to encrypt:")
    for file in files_to_encrypt:
        print(f"  - {file.name} ({file.stat().st_size} bytes)")
    
    print("\nStarting batch encryption...")
    
    success_count = 0
    total_time = 0
    
    for file in files_to_encrypt:
        try:
            print(f"\nProcessing: {file.name}")
            
            encrypted_path = encrypted_dir / f"{file.name}.enc"
            
            start_time = time.time()
            dc.encrypt_file(str(file), str(encrypted_path))
            encrypt_time = time.time() - start_time
            
            total_time += encrypt_time
            success_count += 1
            
            print(f"  ✅ Encrypted in {encrypt_time:.4f}s -> {encrypted_path.name}")
            
        except Exception as e:
            print(f"  ❌ Failed to encrypt {file.name}: {e}")
    
    print(f"\n📊 Batch Encryption Summary:")
    print(f"  Files processed: {success_count}/{len(files_to_encrypt)}")
    print(f"  Total time: {total_time:.4f} seconds")
    print(f"  Average time per file: {total_time/success_count:.4f} seconds")

def different_file_types_demo():
    """Demonstrate encryption of different file types"""
    print("\n" + "="*50)
    print(" Different File Types Demo ")
    print("="*50)
    
    dc = DevCrypt()
    sample_dir = Path("sample_files")
    
    file_types = {
        "Text": "document.txt",
        "JSON": "config.json",
        "Binary": "image.bin",
        "CSV": "data.csv"
    }
    
    for file_type, filename in file_types.items():
        try:
            print(f"\n--- {file_type} File Encryption ---")
            
            input_path = sample_dir / filename
            encrypted_path = sample_dir / f"{filename}.{file_type.lower()}.enc"
            
            if not input_path.exists():
                print(f"  ⚠️ File not found: {filename}")
                continue
            
            # Get file info
            file_size = input_path.stat().st_size
            print(f"  File: {filename}")
            print(f"  Size: {file_size} bytes")
            
            # Encrypt with timing
            start_time = time.time()
            dc.encrypt_file(str(input_path), str(encrypted_path))
            encrypt_time = time.time() - start_time
            
            encrypted_size = encrypted_path.stat().st_size
            size_increase = ((encrypted_size - file_size) / file_size) * 100
            
            print(f"  Encrypted size: {encrypted_size} bytes")
            print(f"  Size increase: {size_increase:.1f}%")
            print(f"  Encryption time: {encrypt_time:.4f}s")
            print(f"  ✅ {file_type} file encrypted successfully")
            
        except Exception as e:
            print(f"  ❌ {file_type} file encryption failed: {e}")

def secure_file_operations():
    """Demonstrate secure file operations"""
    print("\n" + "="*50)
    print(" Secure File Operations Demo ")
    print("="*50)
    
    dc = DevCrypt()
    
    # Create a temporary sensitive file
    sensitive_file = Path("sensitive_data.tmp")
    with open(sensitive_file, "w") as f:
        f.write("EXTREMELY SENSITIVE INFORMATION - DO NOT SHARE!")
    
    print(f"Created sensitive file: {sensitive_file}")
    
    try:
        # Encrypt the file
        encrypted_file = Path("sensitive_data.enc")
        print(f"\nEncrypting to: {encrypted_file}")
        dc.encrypt_file(str(sensitive_file), str(encrypted_file))
        
        # Securely delete the original (simulate)
        print("Securely deleting original file...")
        if sensitive_file.exists():
            # Overwrite with random data multiple times (basic secure delete)
            file_size = sensitive_file.stat().st_size
            with open(sensitive_file, "r+b") as f:
                for _ in range(3):  # Overwrite 3 times
                    f.seek(0)
                    f.write(os.urandom(file_size))
                    f.flush()
                    os.fsync(f.fileno())
            
            sensitive_file.unlink()  # Delete the file
            print("✅ Original file securely deleted")
        
        # Verify encryption worked
        if encrypted_file.exists():
            print("✅ Encrypted file created successfully")
            
            # Try to decrypt and verify
            decrypted_file = Path("sensitive_restored.tmp")
            dc.decrypt_file(str(encrypted_file), str(decrypted_file))
            
            with open(decrypted_file, "r") as f:
                content = f.read()
                if "EXTREMELY SENSITIVE" in content:
                    print("✅ File successfully decrypted and verified")
                else:
                    print("❌ Decrypted file content doesn't match")
            
            # Clean up
            decrypted_file.unlink()
            encrypted_file.unlink()
        
    except Exception as e:
        print(f"❌ Secure file operations failed: {e}")
    
    finally:
        # Clean up any remaining files
        for temp_file in [sensitive_file, Path("sensitive_data.enc"), Path("sensitive_restored.tmp")]:
            if temp_file.exists():
                temp_file.unlink()

def directory_encryption_demo():
    """Demonstrate encrypting entire directories"""
    print("\n" + "="*50)
    print(" Directory Encryption Demo ")
    print("="*50)
    
    dc = DevCrypt()
    source_dir = Path("sample_files")
    encrypted_dir = Path("encrypted_directory")
    decrypted_dir = Path("decrypted_directory")
    
    # Clean up existing directories
    for dir_path in [encrypted_dir, decrypted_dir]:
        if dir_path.exists():
            shutil.rmtree(dir_path)
    
    encrypted_dir.mkdir(exist_ok=True)
    decrypted_dir.mkdir(exist_ok=True)
    
    print(f"Encrypting directory: {source_dir}")
    print(f"Output directory: {encrypted_dir}")
    
    try:
        # Get all files in source directory
        files = list(source_dir.glob("*"))
        files = [f for f in files if f.is_file()]
        
        print(f"Found {len(files)} files to encrypt")
        
        # Encrypt each file
        for file in files:
            encrypted_path = encrypted_dir / f"{file.name}.enc"
            print(f"  Encrypting: {file.name}")
            dc.encrypt_file(str(file), str(encrypted_path))
        
        print("✅ Directory encryption completed")
        
        # Decrypt the directory
        print(f"\nDecrypting directory to: {decrypted_dir}")
        encrypted_files = list(encrypted_dir.glob("*.enc"))
        
        for enc_file in encrypted_files:
            # Remove .enc extension for decrypted file
            original_name = enc_file.name[:-4]  # Remove .enc
            decrypted_path = decrypted_dir / original_name
            
            print(f"  Decrypting: {enc_file.name}")
            dc.decrypt_file(str(enc_file), str(decrypted_path))
        
        print("✅ Directory decryption completed")
        
        # Verify directory contents
        original_files = {f.name: f.stat().st_size for f in files}
        decrypted_files = {f.name: f.stat().st_size for f in decrypted_dir.glob("*") if f.is_file()}
        
        if original_files == decrypted_files:
            print("✅ Directory integrity verified - all files match!")
        else:
            print("❌ Directory integrity check failed")
            print(f"Original: {original_files}")
            print(f"Decrypted: {decrypted_files}")
        
    except Exception as e:
        print(f"❌ Directory encryption failed: {e}")

def cleanup_demo_files():
    """Clean up all demo files and directories"""
    print("\n" + "="*50)
    print(" Cleanup ")
    print("="*50)
    
    directories_to_remove = [
        "sample_files",
        "encrypted_files", 
        "encrypted_directory",
        "decrypted_directory"
    ]
    
    files_to_remove = [
        "sensitive_data.tmp",
        "sensitive_data.enc",
        "sensitive_restored.tmp"
    ]
    
    print("Cleaning up demo files and directories...")
    
    # Remove directories
    for dir_name in directories_to_remove:
        dir_path = Path(dir_name)
        if dir_path.exists() and dir_path.is_dir():
            try:
                shutil.rmtree(dir_path)
                print(f"  ✅ Removed directory: {dir_name}")
            except Exception as e:
                print(f"  ❌ Failed to remove {dir_name}: {e}")
    
    # Remove individual files
    for file_name in files_to_remove:
        file_path = Path(file_name)
        if file_path.exists():
            try:
                file_path.unlink()
                print(f"  ✅ Removed file: {file_name}")
            except Exception as e:
                print(f"  ❌ Failed to remove {file_name}: {e}")
    
    print("Cleanup completed!")

if __name__ == "__main__":
    print("DevCrypt File Encryption Examples")
    print("=" * 60)
    
    try:
        # Create sample files
        sample_dir = create_sample_files()
        
        # Run all demos
        single_file_encryption()
        batch_file_encryption()
        different_file_types_demo()
        secure_file_operations()
        directory_encryption_demo()
        
        # Ask user if they want to keep demo files
        if "--keep-files" not in sys.argv:
            response = input("\nDo you want to keep the demo files? (y/N): ").strip().lower()
            if response not in ['y', 'yes']:
                cleanup_demo_files()
        else:
            print("\nDemo files kept as requested (--keep-files flag used)")
        
        print("\n🔒 File encryption examples completed successfully!")
        print("Your files are now secure with DevCrypt!")
        
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user")
        cleanup_demo_files()
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        cleanup_demo_files()
        sys.exit(1)