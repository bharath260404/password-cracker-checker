# strength_checker.py

# Function to analyze password
def analyze_password(password):
    # Count character types
    upper = sum(1 for c in password if c.isupper())     # A, B, C...
    lower = sum(1 for c in password if c.islower())     # a, b, c...
    digits = sum(1 for c in password if c.isdigit())    # 0-9
    special = sum(1 for c in password if not c.isalnum())  # !, @, #, etc.
    length = len(password)

    # Print the breakdown
    print(f"Password: {password}")
    print(f"Length: {length}")
    print(f"Uppercase Letters: {upper}")
    print(f"Lowercase Letters: {lower}")
    print(f"Digits: {digits}")
    print(f"Special Characters: {special}")

    # Scoring logic
    score = 0
    if length >= 8:
        score += 1
    if upper > 0:
        score += 1
    if lower > 0:
        score += 1
    if digits > 0:
        score += 1
    if special > 0:
        score += 1

    # Rating the password
    if score <= 2:
        print("Strength: ❌ Weak")
        print("Hint: Add special characters and make it longer")
    elif score == 3 or score == 4:
        print("Strength: ⚠️ Medium")
    else:
        print("Strength: ✅ Strong")

# Take user input
if __name__ == "__main__":
    pw = input("Enter a password to check strength: ")
    analyze_password(pw)
