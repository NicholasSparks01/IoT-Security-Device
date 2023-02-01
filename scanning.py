import nmap

# Initialize the nmap scanner
nm = nmap.PortScanner()

# Scan the local network for open ports
nm.scan(hosts='192.168.1.0/24', arguments='-p 22,80')

# Iterate over the scanned hosts
for host in nm.all_hosts():
    print(f"Host: {host}")

    # Check if the host is up
    if nm[host].state() == "up":
        print("  State: Up")

        # Iterate over the open ports on the host
        for port in nm[host]['tcp']:
            print(f"  Port: {port}")
            print(f"  State: {nm[host]['tcp'][port]['state']}")
