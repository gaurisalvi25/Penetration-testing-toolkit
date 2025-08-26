import socket

def port_scan(target, ports):
    print(f"\n[+] Starting port scan on {target}...\n")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            else:
                print(f"[CLOSED] Port {port}")
            sock.close()
        except Exception as e:
            print(f"[ERROR] Could not scan port {port} -> {e}")
