# Link: https://kiminewt.github.io/pyshark/
# Link: https://github.com/KimiNewt/pyshark
# Created by: Nicholas Sparks
import pyshark

capture = pyshark.LiveCapture(interface='Wi-Fi', output_file='Test.cap')
capture.sniff(timeout=20)

