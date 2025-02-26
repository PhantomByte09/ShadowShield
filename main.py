import os
from core.anonymizer import change_mac, change_ip
from core.encryption import encrypt_message, decrypt_message
from core.firewall import activate_firewall

def main():
    print("🛡️ مرحبًا بك في ShadowShield - أداة الأمان المتكاملة")

    # تشغيل الجدار الناري
    activate_firewall()

    # إخفاء MAC Address
    new_mac = change_mac()
    print(f"✅ تم تغيير MAC Address إلى: {new_mac}")

    # تغيير IP Address عبر Tor
    proxy = change_ip()
    print(f"✅ تم تغيير IP Address إلى: {proxy}")

    # تجربة التشفير
    message = input("🔑 أدخل النص لتشفيره: ")
    encrypted = encrypt_message(message)
    print(f"🔒 النص المشفر: {encrypted}")

    decrypted = decrypt_message(encrypted)
    print(f"🔓 النص بعد فك التشفير: {decrypted}")

if __name__ == "__main__":
    main()
