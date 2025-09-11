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

## Labs Left
29 more to go — currently working through core theory + hands-on practice.

