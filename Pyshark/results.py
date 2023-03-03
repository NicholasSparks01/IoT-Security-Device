import pyshark
filtered = 'udp.port == 5353 and mdns contains "Google" or mdns contains "Amazon" or mdns contains "amazon" or mdns contains "google"'
test_filter = 'udp'
PossibleIP = []
# filtered_capture = pyshark.FileCapture('IoT-Security-Device/Pyshark/Test.cap', display_filter= "udp.port == 5353 and mdns contains 'Google' or mdns contains 'amazon'")

for packet in pyshark.FileCapture('Test.cap', display_filter= filtered):
    source_address = packet.ip.src
    print(type(source_address))
    if source_address not in PossibleIP:
        PossibleIP.append(str(source_address))

print(PossibleIP)
    



