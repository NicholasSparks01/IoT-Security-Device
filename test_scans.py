import nmap
import csv
import random

# Initialize the nmap scanner
nm = nmap.PortScanner()

# Scan the local network for open ports
nm.scan(hosts='192.168.1.0/24', arguments='-p 8008, 80, 8008, 8009, 8443, 9000, 10001, 5353, 53')
# Iterate over the scanned hosts
for host in nm.all_hosts():
    print(f"Host: {host}")

    # Check if the host is up
    if nm[host].state() == "up":
        print("  State: Up")

        # Iterate over the open ports on the host
        # Added udp in nm[host][]
        for port in nm[host]['tcp']:
            print(f"  Port: {port}")
            print(f"  State: {nm[host]['tcp'][port]['state']}")

print(nm.csv())
#host;protocol;port;name;state;product;extrainfo;reason;version;conf

# Exporting results to .csv. Maybe works???
with open('nm.csv()', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(nm)
