# 🔐 Password Strength Checker & Cracker (Python)

This is a **Python project** that:
- ✔️ Checks the strength of a password (weak, medium, strong)
- 🔑 Hashes the password using SHA-256 or MD5
- 💣 Demonstrates how weak passwords can be cracked using **dictionary attacks**
- ⚠️ Educates users about real-world password security risks

---

## 📂 Project Structure

password-cracker-checker/
├── main.py # Project launcher
├── strength_checker.py # Checks password strength
├── hasher.py # Hashes passwords using SHA-256 or MD5
├── cracker.py # Cracks password hashes using a wordlist
└── wordlists/
└── rockyou_sample.txt # Sample password dictionary

---

## 🚀 Features

- ✅ Password strength scoring: based on length, uppercase, digits, symbols
- 🔐 Hash conversion using SHA-256 / MD5
- 🧠 Simulated dictionary attack using a sample wordlist
- ⏱ Time-based cracking simulation to compare weak vs strong passwords

---

## 🧪 Sample Output

Enter a password: admin123
Strength: ⚠️ Medium
SHA-256: 8c6976e5b5410415bde908bd4dee15dfb16bfae...
Trying to crack hash using dictionary...
✅ Password cracked: admin123

---

## 🛠️ Technologies Used

- Python 3.x
- `hashlib` (for hashing)
- `time` (for attack simulation)
- `file I/O` (for reading dictionary files)

---

## 🎓 What I Learned

- Basics of **password security and cracking**
- Real-world use of **hash functions**
- How brute force and dictionary attacks work
- Why strong passwords matter 🔐

---

## ⚠️ Disclaimer

This project is for **educational purposes only.**  
Do **not** use these techniques on any system you don’t own or have permission to test. ❌

---

## 📌 Author

**Bharath**  
- 💼 Aspiring Cybersecurity Enthusiast  
- 📧 bobbyyyyy2604@gmail.com

---

## 🌟 Star this repo if you liked it!
