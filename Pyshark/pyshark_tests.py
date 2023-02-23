# Link: https://kiminewt.github.io/pyshark/
# Link: https://github.com/KimiNewt/pyshark
# Created by: Nicholas Sparks
import pyshark

capture = pyshark.LiveCapture(interface='Wi-Fi')# eth0 can be changed

# capture.sniff(timeout=10)
# capture

for packet in capture.sniff_continuously(packet_count=2):
    print(f'Packet: {packet}')



# for packet in capture:
#     print(f'Packet: {packet}')




