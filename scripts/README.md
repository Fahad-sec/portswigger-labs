# SQLI Automation Scripts
- This folder contains python scripts I wrote to automate parts of the PortSwigger Web Security Academy SQL Injection Labs.
- They are for learning puposes only, designed to demonstrate how SQL injection Payloads can be automated with python.

## Scripts
1. **sqli_password_extractor_response.py**
- Type: Blind SQL Injection (Response-based)
- Working:
     - Automates guessing an administrator password character by character.
     - Uses conditional payloads inside a cookie (TrackingId) and checks the server's HTTP response to confirm guesses.
- Success condition: Script looks for the text "Welcome back" in the response.

2. **sqli_password_extractor_error.py**
- Type: Blind SQL Injection (ERR-BASED)
- Working:
     -  Automates guessing an administrator password character by character.
     -  Payloads are crafted so that a **corrent guess triggers a database error**
     -  The script confirms guesses by checking for an HTTP '500' response.
- Success condition: Script identifies a match when the server responds with the '500' Server error.
3. **blind_sqli_delay_extract.py**
- Type: Blind SQL Injection (Time-based)
- Working:
     - Automates extracting the administrator password one character at a time.
     - Injecting payloads into the 'TrackingId' cookie that use PostgreSQL's 'pg_sleep()' to cause a        time delay when the guessed character is correct.
     - Measures response time to determine correct guesses.
- Success condition: A correct guess makes the server delay the response (>3s), which confirms the character.

## Notes
- These scripts are tied to only specific PortSwigger Labs.
- The purpose was to practice Python and SQLI logic and not to build tools.
- They show the difference between exploiting response-based and error-based SQLi conditions.

## Disclaimer: These scripts are for learning and labs only and not to be used illegally.
