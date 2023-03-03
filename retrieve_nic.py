import ifaddr

wifi_interface_name = None

# Get a list of all network interfaces on the system
adapters = ifaddr.get_adapters()

# Loop through the adapters and find the WiFi interface
for adapter in adapters:
    # if adapter.ips and "wlan" in adapter.nice_name:
    #     wifi_interface_name = adapter.nice_name
    #     break
    print(adapter)

# Print the name of the WiFi interface, if it was found
if wifi_interface_name:
    print(f"WiFi interface name: {wifi_interface_name}")
else:
    print("No WiFi interface found")