# Recon Tool

This is a Python-based command-line reconnaissance tool built for offensive security and penetration testing tasks. It automates the information gathering phase by collecting useful data about a target domain.

## What the Tool Does

The tool performs both passive and active reconnaissance. Each module can be used independently through command-line flags.

## Modules Included

1. **WHOIS Lookup**  
   Retrieves domain registration details such as registrar, creation and expiry dates, and contact info.

2. **DNS Enumeration**  
   Resolves DNS records (A, MX, NS, and TXT) using `dnspython`.

3. **Subdomain Enumeration**  
   Uses the crt.sh certificate transparency API to find subdomains of the target domain.

4. **Port Scanning**  
   Scans a list of common TCP ports and identifies which ones are open using Python sockets.

5. **Banner Grabbing**  
   Connects to open ports and attempts to fetch service banners (e.g., HTTP headers, FTP greetings).

6. **Technology Detection**  
   Uses the `whatweb` tool to detect underlying technologies used by a website (e.g., WordPress, Apache, nginx, etc.).

7. **Report Generation**  
   Generates a `.txt` report of all findings with timestamps and resolved IP.

---

## Installation

### Clone and set up the virtual environment:

```bash
git clone https://github.com/bakhtawere/recon-tool.git
cd recon-tool
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Make sure WhatWeb is installed:
```bash
sudo apt install whatweb
```
Usage
Run the tool with the desired flags. You can mix multiple options in a single command.

```bash
python3 main.py github.com --whois --dns --subs --ports --banner --tech --report github_report.txt
```
### Available Options

| Flag       | Description                                   |
|------------|-----------------------------------------------|
| `--whois`  | Perform WHOIS lookup                          |
| `--dns`    | Fetch A, MX, NS, and TXT DNS records          |
| `--subs`   | Find subdomains using crt.sh                  |
| `--ports`  | Scan common TCP ports                         |
| `--banner` | Grab service banners from open ports          |
| `--tech`   | Detect web technologies via WhatWeb           |
| `--report` | Save output to a report file                  |

---

### Output

The tool prints results in the terminal and optionally writes them to a `.txt` file.

Each report includes:

- Domain IP resolution  
- Date and time  
- Output from each selected module  

---

### Notes

Developed as part of a cybersecurity internship project (ITSOLERA Cyber Department).

> **Use this tool only on domains you are authorized to test.**
