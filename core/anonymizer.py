import os
import random

def change_mac(interface="wlan0"):
    """يغير عنوان MAC لإخفاء الهوية"""
    new_mac = "00:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0, 255) for _ in range(5))
    os.system(f"ifconfig {interface} down")
    os.system(f"ifconfig {interface} hw ether {new_mac}")
    os.system(f"ifconfig {interface} up")
    return new_mac

def change_ip():
    """يستخدم Tor لتغيير عنوان الـ IP"""
    os.system("systemctl restart tor")
    return "socks5h://127.0.0.1:9050"
