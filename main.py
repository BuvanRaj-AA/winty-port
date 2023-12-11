import socket

def port_scan_with_banner(target, ports):
    print(f"Scanning target: {target}")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        try:
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: Open")
                sock.send(b"Hello\r\n")
                banner = sock.recv(1024)
                print(f"Banner for Port {port}: {banner.decode().strip()}")
            else:
                print(f"Port {port}: Closed")
            sock.close()
        except socket.error:
            print("Socket error occurred.")

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    port_range = input("Enter port range to scan (e.g., '1-1000'): ")
    start_port, end_port = map(int, port_range.split('-'))
    ports_to_scan = range(start_port, end_port + 1)
    port_scan_with_banner(target_ip, ports_to_scan)
