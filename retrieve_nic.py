import platform
import subprocess
import wmi

def get_wifi_interface_windows():
    c = wmi.WMI()
    interfaces = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    for interface in interfaces:
        if interface.Description.startswith("Intel(R) Dual Band Wireless"):
            return interface.Description
    return None

def get_wifi_interface_linux():
    try:
        output = subprocess.check_output(["iwconfig"]).decode("utf-8").strip()
        interfaces = output.split("\n")
        for interface in interfaces:
            if "wlp" in interface:
                return interface.split()[0]
    except subprocess.CalledProcessError:
        return None

def get_wifi_interface():
    if platform.system() == "Windows":
        return get_wifi_interface_windows()
    else:
        return get_wifi_interface_linux()

wifi_interface = get_wifi_interface()
if wifi_interface:
    print("Wi-Fi interface:", wifi_interface)
else:
    print("No Wi-Fi interface found")
