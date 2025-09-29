# PortSwigger Labs Progress(Total labs completed: 61)
Progress tracker for PortSwigger Web Security Academy labs — documented hands-on practice in SQLi + automation scripts.

## SQL Injection (SQLI): 16/18

## Completed Labs 

Apprentice
- SQL injection vulnerability in WHERE clause allowing retrieval of hidden data
- SQL injection vulnerability allowing login bypass

**Practitioner**
- SQL injection attack, querying the database type and version on Oracle
- SQL injection attack, querying the database type and version on MySQL and Microsoft  
- SQL injection attack, listing the database contents on non-Oracle databases  
- SQL injection attack, listing the database contents on Oracle  
- SQL injection UNION attack, determining the number of columns returned by the query  
- SQL injection UNION attack, finding a column containing text  
- SQL injection UNION attack, retrieving data from other tables  
- SQL injection UNION attack, retrieving multiple values in a single column  
- Blind SQL injection with conditional responses  
- Blind SQL injection with conditional errors  
- Visible error-based SQL injection  
- Blind SQL injection with time delays
- Blind SQL injection with time delays and information retrieval
- SQL injection with filter bypass via XML encoding 

## Labs Left

**Practitioner**
- Blind SQL injection with out-of-band interaction *(requires Burp Suite Professional)*
- Blind SQL injection with out-of-band data exfiltration *(requires Burp Suite Professional)*

**See the automation scripts:** the `scripts/` folder contains demo scripts for response-based, error-based, and time-delay SQLi extraction. 
Browse: [./scripts](./scripts/)

---

## Cross-Site Scripting (XSS): 28/30
Tracking hands-on labs and payload crafting for different XSS contexts.

## Completed Labs

Apprentice(COMPLETED)
- Reflected XSS into HTML context with nothing encoded
- Stored XSS into HTML context with nothing encoded
- DOM XSS in document.write sink using source location.search
- DOM XSS in innerHTML sink using source location.search
- DOM XSS in jQuery anchor href attribute sink using location.search source
- DOM XSS in jQuery selector sink using a hashchange event
- Reflected XSS into attribute with angle brackets HTML-encoded
- Stored XSS into anchor href attribute with double quotes HTML-encoded
- Reflected XSS into a JavaScript string with angle brackets HTML encoded

Practitioner(COMPLETED)
- DOM XSS in document.write sink using source location.search inside a select element
- DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded
- Reflected DOM XSS
- Stored DOM XSS
- Reflected XSS into HTML context with most tags and attributes blocked
- Reflected XSS into HTML context with all tags blocked except custom ones
- Reflected XSS with some SVG markup allowed
- Reflected XSS in canonical link tag
- Reflected XSS into a JavaScript string with single quote and backslash escaped
- Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped
- Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped
- Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped
- Exploiting cross-site scripting to steal cookies
- Exploiting cross-site scripting to capture passwords
- Exploiting XSS to bypass CSRF defenses

EXPERT
- Reflected XSS with AngularJS sandbox escape without strings
- Reflected XSS with AngularJS sandbox escape and CSP
- Reflected XSS with event handlers and href attributes blocked
- Reflected XSS in a JavaScript URL with some characters blocked

## Access control vulnerabilities: (13/13)
- Unprotected admin functionality
- Unprotected admin functionality with unpredictable URL
- User role controlled by request parameter
- User role can be modified in user profile
- User ID controlled by request parameter
- User ID controlled by request parameter, with unpredictable user IDs
- User ID controlled by request parameter with data leakage in redirect
- User ID controlled by request parameter with password disclosure
- Insecure direct object references
- URL-based access control can be circumvented
- Method-based access control can be circumvented
- Multi-step process with no access control on one step
- Referer-based access control
