# main.py

from strength_checker import analyze_password
from hasher import hash_password
from cracker import dictionary_attack

def main():
    print("🔐 Welcome to Password Security Demo\n")

    password = input("👉 Enter a password to analyze: ")

    print("\n📊 Password Strength Checker:")
    analyze_password(password)

    # Hash password
    print("\n🔑 Generating Hashes...")
    md5_hash = hash_password(password, 'md5')
    sha256_hash = hash_password(password, 'sha256')

    print(f"MD5:     {md5_hash}")
    print(f"SHA-256: {sha256_hash}")

    # Ask user if they want to crack
    choice = input("\n💣 Simulate dictionary attack on this password? (yes/no): ").lower()
    if choice == "yes":
        algo = input("Hash method to crack? (md5/sha256): ").lower()
        if algo == "md5":
            print("\n🚨 Trying to crack MD5 hash...")
            dictionary_attack(md5_hash, 'md5')
        elif algo == "sha256":
            print("\n🚨 Trying to crack SHA-256 hash...")
            dictionary_attack(sha256_hash, 'sha256')
        else:
            print("❌ Unsupported method.")
    else:
        print("✅ Skipped cracking simulation.")

    print("\n✅ Demo complete. Stay safe online!")

if __name__ == "__main__":
    main()
