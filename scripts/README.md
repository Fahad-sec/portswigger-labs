# SQLI Automation Scripts
- This folder contains python scripts I wrote to automate parts of the PortSwigger Web Security Academy SQL Injection Labs.
- They are for learning puposes only, designed to demonstrate how SQL injection Payloads can be automated with python.

## Scripts
1. **sqli_password_extractor_response.py
- Type: Blind SQL Injection (Response-based)
- Working:
     - Automated guessing an administrator password character by character.
     - Uses conditional payloads inside a cookie (TrackingId) and checks the server's HTTP response to confirm guesses.
- Success condition: Script looks for the text "Welcome back" in the response.

## Notes
- These scripts are tied to only specific PortSwigger Labs.
- The purpose was to practice Python and SQLI logic and not to build tools.
- They show the difference between exploiting response-based and error-based SQLi conditions.

## Disclaimer: These scripts are for learning and labs only and not to be used illegally.
