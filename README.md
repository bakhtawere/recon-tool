# Recon Tool

This is a Python-based command-line reconnaissance tool created for offensive security and penetration testing tasks. It automates the information gathering phase by collecting useful data about a target domain.

## What the Tool Does

This tool performs both passive and active reconnaissance and supports multiple modules:

## Modules Included

1. **WHOIS Lookup**  
   Retrieves domain registration details such as registrar, creation/expiry dates, and owner info.

2. **DNS Enumeration**  
   Resolves DNS records: A, MX, NS, and TXT using dnspython.

3. **Subdomain Enumeration**  
   Uses the crt.sh certificate transparency API to find subdomains related to the main domain.

4. **Port Scanning**  
   Scans common TCP ports (e.g., 80, 443, 21, 22, etc.) using Python sockets and shows which are open.

5. **Banner Grabbing**  
   Connects to open ports and attempts to retrieve service banners (e.g., HTTP headers, FTP greetings).

6. **Technology Detection**  
   Uses the whatweb tool to identify web technologies (e.g., WordPress, nginx, jQuery, etc.).

7. **Report Generation**  
   Saves the collected data in a text file report with timestamp and resolved IP.

## How to Use

### 1. Install Python Dependencies

pip install -r requirements.txt

Make sure you are using Python 3 and have whatweb installed (already available in Kali Linux).

2. Activate Virtual Environment

source venv/bin/activate
3. Run the Tool

python3 main.py [domain] [options]
Example

python3 main.py github.com --whois --dns --subs --ports --banner --tech --report github_report.txt
This will run all modules and save results to github_report.txt.

Available Options
Flag	Description
--whois	Perform WHOIS lookup
--dns	Fetch A, MX, NS, and TXT DNS records
--subs	Find subdomains using crt.sh
--ports	Scan a list of common TCP ports
--banner	Grab service banners from open ports
--tech	Detect technologies using WhatWeb
--report FILE	Save results to a .txt report file

Output
The tool prints results in the terminal and optionally saves them to a file.

The report includes:

Domain IP resolution

Date and time

Results from each selected module

Note
This tool was developed as part of a cybersecurity internship project (ITSOLERA Cyber Department). Use it only on domains you are authorized to test.
