from Crypto.Cipher import AES
import hashlib
import os
import sys

def enc(data, key, iv, filepath):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    enc_data = cipher.encrypt(data)

    with open(os.path.join(filepath, "encrypted.enc"), "wb") as file:
        file.write(enc_data)

def dec(data, key, iv, filepath):
    decipher = AES.new(key, AES.MODE_CFB, iv)
    data = decipher.decrypt(data)

    with open(os.path.join(filepath, "decrypted.png"), "wb") as file:
        file.write(data)
def main():
    if len(sys.argv) < 3:
        print("Usage: python encrypt_decrypt.py <encrypt/decrypt> <file_path>")
        return
    
    mode = sys.argv[1].lower()
    file_path = sys.argv[2]

    if mode == "encrypt":
        password = input("Enter Encryption Password: ")
        key = hashlib.sha256(password.encode()).digest()
        iv = key[:16]

        with open(file_path, 'rb') as f:
            input_data = f.read()
        enc(input_data, key, iv, os.path.dirname(file_path))
        print("Encryption successful. File stored as: encrypted.enc")

    elif mode == "decrypt":
        password = input("Enter Decryption Password: ")
        key = hashlib.sha256(password.encode()).digest()
        iv = key[:16]

        with open(file_path, 'rb') as f:
            input_data = f.read()
        dec(input_data, key, iv, os.path.dirname(file_path))
        print("Decryption successful. File stored as: decrypted.png")

    else:
        print("Invalid mode. Please use 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
