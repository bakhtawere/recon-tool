import requests

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return [f"[!] crt.sh returned status {response.status_code}"]

        data = response.json()
        subdomains = set()
        for entry in data:
            name = entry.get("name_value", "")
            if domain in name:
                for sub in name.split("\n"):
                    subdomains.add(sub.strip())

        return sorted(subdomains)
    except Exception as e:
        return [f"[!] Failed to fetch subdomains: {e}"]
