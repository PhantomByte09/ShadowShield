import os
from cryptography.fernet import Fernet

# إنشاء مفتاح تشفير AES
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# تحميل مفتاح التشفير
def load_key():
    return open("key.key", "rb").read()

# تشفير النصوص
def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

# فك تشفير النصوص
def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message

if __name__ == "__main__":
    if not os.path.exists("key.key"):
        generate_key()

    key = load_key()
    
    message = input("🔑 أدخل النص لتشفيره: ")
    encrypted = encrypt_message(message, key)
    print(f"🔒 النص المشفر: {encrypted}")

    decrypted = decrypt_message(encrypted, key)
    print(f"🔓 النص بعد فك التشفير: {decrypted}")
