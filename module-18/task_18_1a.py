import yaml
from netmiko import ConnectHandler, NetmikoAuthenticationException, NetmikoTimeoutException

def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            output = ssh.send_command(command)
            return output
    except NetmikoAuthenticationException as auth_err:
        print(f"[AUTH ERROR] Failed to authenticate on {device['host']}: {auth_err}")
    except NetmikoTimeoutException as time_err:
        print(f"[TIMEOUT ERROR] Connection timed out for {device['host']}: {time_err}")
    except Exception as err:
        print(f"[ERROR] An unexpected error occurred on {device['host']}: {err}")

if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(f"--- Checking {dev['host']} ---")
        send_show_command(dev, command)
