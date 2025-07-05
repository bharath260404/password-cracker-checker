# hasher.py
import hashlib

def hash_password(password, method='sha256'):
    if method == 'sha256':
        hashed = hashlib.sha256(password.encode()).hexdigest()
    elif method == 'md5':
        hashed = hashlib.md5(password.encode()).hexdigest()
    else:
        raise ValueError("Unsupported hashing method")

    return hashed

if __name__ == "__main__":
    pw = input("Enter a password to hash: ")
    print("SHA-256 Hash:", hash_password(pw, 'sha256'))
    print("MD5 Hash:", hash_password(pw, 'md5'))
