import socket

def scan_ports(target, ports=[21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 8080]):
    open_ports = []

    print(f"[~] Scanning {target} for common ports...\n")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"
                open_ports.append((port, service))
            sock.close()
        except:
            continue

    return open_ports
