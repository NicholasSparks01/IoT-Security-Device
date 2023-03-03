# Link: https://kiminewt.github.io/pyshark/
# Link: https://github.com/KimiNewt/pyshark
# Created by: Nicholas Sparks
import pyshark

# capture = pyshark.LiveCapture(interface='Wi-Fi', output_file='Test.cap')
# capture.sniff(timeout=20)
PossibleIP = []
WiresharkFilter = 'udp.port == 5353 and mdns contains "Google" or mdns contains "Amazon" or mdns contains "amazon" or mdns contains "google"'

def Live_Capture():
    capture = pyshark.LiveCapture(interface='Wi-Fi', output_file='Test.cap')
    capture.sniff(timeout=20)

def Packet_Analysis():
    for packet in pyshark.FileCapture('Test.cap', display_filter= WiresharkFilter):
        source_address = packet.ip.src
        # print(type(source_address))
        if source_address not in PossibleIP:
            PossibleIP.append(str(source_address))
    return PossibleIP


Live_Capture()
list = Packet_Analysis()
print(list)