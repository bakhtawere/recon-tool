import socket

def grab_banner(ip, port, timeout=2):
    try:
        sock = socket.socket()
        sock.settimeout(timeout)
        sock.connect((ip, port))
        banner = sock.recv(1024)
        sock.close()
        return banner.decode(errors="ignore").strip()
    except Exception as e:
        return f"[!] No banner or error on port {port}: {e}"
