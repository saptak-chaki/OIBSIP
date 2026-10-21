import socket
from datetime import datetime

def main():
    print("==========================================")
    print("         Basic Python Port Scanner        ")
    print("==========================================")
    
    target_host = input("Enter target IP address or domain (e.g., 127.0.0.1): ")
    
    print("-" * 50)
    print(f"Scanning target: {target_host}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)
    
    try:
        # Scanning common ports (e.g., 21, 22, 80, 443)
        common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 8080]
        
        for port in common_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target_host, port))
            
            if result == 0:
                print(f"🟢 Port {port}: OPEN")
            else:
                print(f"🔴 Port {port}: Closed")
            s.close()
            
    except KeyboardInterrupt:
        print("\nExiting script. User interrupted.")
    except socket.gaierror:
        print("\n❌ Hostname could not be resolved.")
    except socket.error:
        print("\n❌ Could not connect to server.")
        
    print("==========================================")

if __name__ == "__main__":
    main()