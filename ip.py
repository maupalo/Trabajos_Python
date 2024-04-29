import socket
import netifaces

def check_server(ip, port):
    try:
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set a timeout in case the connection takes too long
            s.settimeout(1)
            # Try to connect to the server
            s.connect((ip, port))
            # If connection successful, return True
            return True
    except Exception as e:
        # If any exception occurs (connection refused, timeout, etc.), return False
        return False

def get_local_ips():
    ips = []
    for interface in netifaces.interfaces():
        try:
            addresses = netifaces.ifaddresses(interface)
            ip = addresses[netifaces.AF_INET][0]['addr']
            ips.append(ip)
        except KeyError:
            pass
    return ips

def main():
    # Get local IP addresses
    ips = get_local_ips()
    
    # Port to check
    port = 3000
    
    # Check each local IP address
    for ip in ips:
        if check_server(ip, port):
            print(f"Server found at {ip}:{port}")
        else:
            print(f"No server found at {ip}:{port}")

if __name__ == "__main__":
    main()
