import dns.resolver

def get_dns_records(domain):
    records = {}
    try:
        records["A"] = [r.address for r in dns.resolver.resolve(domain, "A")]
    except:
        records["A"] = ["No A record found."]
    
    try:
        records["MX"] = [str(r.exchange) for r in dns.resolver.resolve(domain, "MX")]
    except:
        records["MX"] = ["No MX record found."]
    
    try:
        records["NS"] = [str(r.target) for r in dns.resolver.resolve(domain, "NS")]
    except:
        records["NS"] = ["No NS record found."]
    
    try:
        records["TXT"] = [str(r.strings[0], 'utf-8') for r in dns.resolver.resolve(domain, "TXT")]
    except:
        records["TXT"] = ["No TXT record found."]
    
    return records
