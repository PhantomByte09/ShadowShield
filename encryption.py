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
def encrypt_message(message):
    key = load_key()
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())

# فك تشفير النصوص
def decrypt_message(encrypted_message):
    key = load_key()
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message).decode()
