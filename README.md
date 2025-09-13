# PortSwigger Labs Progress
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

## Cross-Site Scripting (XSS): 1/30
Tracking hands-on labs and payload crafting for different XSS contexts.

## Completed Labs

Apprentice
- Reflected XSS into HTML context with nothing encoded
- Stored XSS into HTML context with nothing encoded
- DOM XSS in document.write sink using source location.search
- DOM XSS in innerHTML sink using source location.search
- DOM XSS in jQuery anchor href attribute sink using location.search source
- DOM XSS in jQuery selector sink using a hashchange event
- Reflected XSS into attribute with angle brackets HTML-encoded
- Stored XSS into anchor href attribute with double quotes HTML-encoded
- Reflected XSS into a JavaScript string with angle brackets HTML encoded

## Labs Left
21 more to go — currently working through core theory + hands-on practice.

