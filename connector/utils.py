from .drivers import ssh, ping


def run_command(ipaddress, command):
    result = []
    result.append(ssh.ssh(ipaddress, command))

    return result


def basic_check(ipaddress):
    commands = ['ifconfig', 'iptables -L -n', 'cat /etc/resolv.conf', 'netstat -nr', 'backone peers']
    result = []

    for command in commands:
        result.append(ssh.ssh(ipaddress, command))

    return result
