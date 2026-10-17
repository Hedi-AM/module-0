from pprint import pprint
import yaml
from netmiko import ConnectHandler

def send_show_command(device, command):
    """Connects to one device via Netmiko and executes a command."""
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()  # Switch to enable mode if needed
            output = ssh.send_command(command)
            return output
    except Exception as error:
        return f"Error connecting to {device['host']}: {error}"

if __name__ == "__main__":
    command = "sh ip int br"

    # Load devices from devices.yaml
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(f"--- Output for {dev['host']} ---")
        result = send_show_command(dev, command)
        print(result)
