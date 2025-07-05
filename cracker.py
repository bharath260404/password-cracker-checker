# cracker.py
import hashlib
import time

def load_wordlist(path):
    with open(path, "r", encoding="latin-1") as f:
        return [line.strip() for line in f.readlines()]

def dictionary_attack(target_hash, method='sha256', wordlist_path='wordlists/rockyou_sample.txt'):
    words = load_wordlist(wordlist_path)
    start = time.time()
    for word in words:
        if method == 'sha256':
            hashed = hashlib.sha256(word.encode()).hexdigest()
        elif method == 'md5':
            hashed = hashlib.md5(word.encode()).hexdigest()
        else:
            raise ValueError("Unknown hash method")

        if hashed == target_hash:
            end = time.time()
            print(f"✅ Password cracked! It was: '{word}'")
            print(f"⏱️ Time taken: {end - start:.2f} seconds")
            return

    print("❌ Password not found in wordlist.")

if __name__ == "__main__":
    hash_input = input("Enter hash to crack: ")
    method = input("Enter method (sha256 or md5): ")
    dictionary_attack(hash_input, method)
