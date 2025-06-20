from datetime import datetime
import socket

def generate_report(domain, data, output="report.txt"):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ip = socket.gethostbyname(domain)
        
        with open(output, "w") as f:
            f.write(f"Recon Report for {domain}\n")
            f.write(f"Resolved IP: {ip}\n")
            f.write(f"Generated on: {timestamp}\n")
            f.write("="*60 + "\n\n")

            for section, content in data.items():
                f.write(f"## {section.upper()} ##\n")
                if isinstance(content, list):
                    for item in content:
                        f.write(f"- {item}\n")
                else:
                    f.write(str(content) + "\n")
                f.write("\n")

        return f"[+] Report saved to {output}"
    except Exception as e:
        return f"[!] Failed to generate report: {e}"

