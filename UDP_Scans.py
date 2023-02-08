# from https://pypi.org/project/python3-nmap/

import nmap3

nmap = nmap3.NmapScanTechniques()

result = nmap.nmap_udp_scan("192.168.1.0/24", args="-p 80, 8008")



