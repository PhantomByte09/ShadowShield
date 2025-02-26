import os
from core.anonymizer import change_mac, change_ip
from core.encryption import encrypt_message, decrypt_message
from core.firewall import activate_firewall

def main():
    print("🛡️ Bienvenue sur ShadowShield - Outil de Protection Avancée")

    # Activation du pare-feu
    activate_firewall()

    # Masquage de l'adresse MAC
    new_mac = change_mac()
    print(f"✅ Adresse MAC modifiée : {new_mac}")

    # Changement de l'adresse IP via Tor
    proxy = change_ip()
    print(f"✅ Adresse IP modifiée via Tor : {proxy}")

    # Test du chiffrement
    message = input("🔑 Entrez un message à chiffrer : ")
    encrypted = encrypt_message(message)
    print(f"🔒 Message chiffré : {encrypted}")

    decrypted = decrypt_message(encrypted)
    print(f"🔓 Message déchiffré : {decrypted}")

if __name__ == "__main__":
    main()
