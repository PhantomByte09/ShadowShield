import unittest
from core.encryption import encrypt_message, decrypt_message

class TestEncryption(unittest.TestCase):
    def test_encryption_decryption(self):
        message = "Hello, ShadowShield!"
        encrypted = encrypt_message(message)
        decrypted = decrypt_message(encrypted)
        self.assertEqual(decrypted, message)

if __name__ == "__main__":
    unittest.main()
