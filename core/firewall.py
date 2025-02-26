import os

def activate_firewall():
    """يقوم بتشغيل جدار الحماية لمنع الهجمات"""
    os.system("ufw enable")
    print("🛡️ تم تفعيل الجدار الناري (Firewall)")
