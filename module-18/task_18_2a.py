import yaml
from netmiko import ConnectHandler


def send_config_commands(device, config_commands, log=True):
    if log:
        print(f"Connecting to {device['host']}...")
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        return ssh.send_config_set(config_commands)


if __name__ == "__main__":
    commands = [
        "logging 10.255.255.1",
        "logging buffered 20010",
        "no logging console",
    ]
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        print(send_config_commands(dev, commands))
