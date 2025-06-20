import report_generator
import argparse
import socket
from modules import whois_lookup, dns_enum, subdomains, port_scan, banner_grab, tech_detect

def main():
    parser = argparse.ArgumentParser(description="Pucho's Recon Tool")
    parser.add_argument("domain", help="Target domain (e.g., tesla.com)")
    parser.add_argument("--whois", action="store_true", help="Perform WHOIS lookup")
    parser.add_argument("--dns", action="store_true", help="Perform DNS enumeration")
    parser.add_argument("--subs", action="store_true", help="Perform subdomain enumeration")
    parser.add_argument("--ports", action="store_true", help="Scan common ports")
    parser.add_argument("--banner", action="store_true", help="Grab banners from open ports")
    parser.add_argument("--tech", action="store_true", help="Detect technologies (via whatweb)")
    parser.add_argument("--report", help="Save results to a report file (e.g., output.txt)")

    args = parser.parse_args()
    domain = args.domain

    if args.whois:
        print("\n[+] WHOIS Lookup Result:")
        result = whois_lookup.perform_whois(domain)
        print(result)

    if args.dns:
        print("\n[+] DNS Enumeration Result:")
        dns_result = dns_enum.get_dns_records(domain)
        for record_type, values in dns_result.items():
            print(f"{record_type} Records:")
            for val in values:
                print(f"  - {val}")
    if args.subs:
        print("\n[+] Subdomain Enumeration (crt.sh):")
        subs = subdomains.get_subdomains(domain)
        for s in subs:
            print(f"  - {s}")
    if args.ports:
        print("\n[+] Port Scan Result:")
        try:
            ip = socket.gethostbyname(domain)
            results = port_scan.scan_ports(ip)
            for port, service in results:
                print(f"  - Port {port}/tcp ({service}) is OPEN")
            if not results:
                print("  No open common ports found.")
        except Exception as e:
            print(f"[!] Failed to scan ports: {e}")
    if args.banner:
        print("\n[+] Banner Grabbing:")
        try:
            ip = socket.gethostbyname(domain)
            ports = [21, 22, 23, 25, 80, 110, 143, 443, 3306]
            for port in ports:
                banner = banner_grab.grab_banner(ip, port)
                if "No banner" not in banner and banner:
                    print(f"  - {port}/tcp: {banner}")
        except Exception as e:
            print(f"[!] Banner grabbing failed: {e}")
    if args.tech:
        print("\n[+] Technology Detection (WhatWeb):")
        output = tech_detect.detect_tech(domain)
        print(output)
    
    # Create report dictionary
    report_data = {}

    if args.whois:
        result = whois_lookup.perform_whois(domain)
        report_data["WHOIS"] = result

    if args.dns:
        dns_result = dns_enum.get_dns_records(domain)
        report_data["DNS Records"] = dns_result

    if args.subs:
        subs = subdomains.get_subdomains(domain)
        report_data["Subdomains"] = subs

    if args.ports:
        ip = socket.gethostbyname(domain)
        port_results = port_scan.scan_ports(ip)
        report_data["Open Ports"] = [f"{p}/tcp ({s})" for p, s in port_results]

    if args.banner:
        ip = socket.gethostbyname(domain)
        ports = [21, 22, 23, 25, 80, 110, 143, 443, 3306]
        banners = []
        for port in ports:
            b = banner_grab.grab_banner(ip, port)
            if "No banner" not in b and b:
                banners.append(f"{port}/tcp: {b}")
        report_data["Banners"] = banners

    if args.tech:
        output = tech_detect.detect_tech(domain)
        report_data["Technologies"] = output

    # Generate report file
    if args.report:
        status = report_generator.generate_report(domain, report_data, args.report)
        print("\n" + status)


if __name__ == "__main__":
    main()


