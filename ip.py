import socket

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

def main():
    # List of IP addresses to check
    ips = [
        "192.168.27.102", "192.168.27.103", "192.168.27.109", "192.168.27.113",
        "192.168.27.118", "192.168.27.121", "192.168.27.135", "192.168.27.142",
        "192.168.27.144", "192.168.27.146", "192.168.27.147", "192.168.27.148",
        "192.168.27.157", "192.168.27.158", "192.168.27.169", "192.168.27.170",
        "192.168.27.178", "192.168.27.179", "192.168.27.181", "192.168.27.182",
        "192.168.27.188", "192.168.27.191", "192.168.27.202", "192.168.27.213",
        "192.168.27.219", "192.168.27.230", "192.168.27.237", "192.168.27.249"
    ]
    
    # Port to check
    port = 80
    
    # Check each IP address
    for ip in ips:
        if check_server(ip, port):
            print(f"Server found at {ip}:{port}")
        #else:
        #    print(f"")

if __name__ == "__main__":
    main()
