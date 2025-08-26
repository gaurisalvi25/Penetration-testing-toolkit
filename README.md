# Penetration Testing Toolkit

A modular Python-based toolkit for penetration testing practice.  
This project demonstrates how security tools like port scanners and brute forcers work under the hood.  
**Educational use only. Do not use against systems you don’t own or have explicit permission to test.**

---

## Features
- **Port Scanner**  
  - Scan specified IP and ports to detect open services.  
  - Helps with reconnaissance and footprinting.

- **Brute Force Tool**  
  - Attempt password brute-force on a demo login form using a wordlist.  
  - Simulates real-world password attack techniques.

- **Modular Design**  
  - Easy to extend with new penetration testing modules (e.g., directory brute-forcing, banner grabbing).

---

## Project Structure
pen_test_toolkit/

│── main.py # Entry point, handles CLI commands

│── scanner.py # Port scanning module

│── bruteforcer.py # Brute force login module

│── app.py # Demo vulnerable Flask login app

│── passwords.txt # Sample wordlist for brute force

│── requirements.txt # Python dependencies


---

## Installation & Setup

1. **Clone this repository**

   git clone https://github.com/<your-username>/pen-test-toolkit.git
   
   cd pen-test-toolkit

2. **Create and activate virtual environment (optional but recommended)**

 python -m venv venv
 
source venv/bin/activate   # On Linux/Mac

venv\Scripts\activate      # On Windows

3. **Install dependencies**

   pip install -r requirements.txt

---

## Usage

1. Run Port Scanner

python main.py scan 127.0.0.1 --ports 22 80 8000
   
2. Run Brute Force Attack

First, start the demo vulnerable app:

python app.py

Then run the brute force module:

python main.py bruteforce http://127.0.0.1:5000/login admin passwords.txt

---

## Disclaimer

This toolkit is created for learning purposes only.
Using it against systems without permission is illegal and unethical.
Use responsibly on your own test environments, labs, or with explicit authorization.

---

## Future Enhancements

Directory brute-forcing module

Service banner grabbing

SQL Injection tester

Password hash cracker

---

## Author

gaurisalvi25
