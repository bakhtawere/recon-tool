import subprocess

def detect_tech(domain):
    try:
        result = subprocess.run(["whatweb", domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"[!] whatweb error: {result.stderr.strip()}"
    except Exception as e:
        return f"[!] Failed to run whatweb: {e}"
