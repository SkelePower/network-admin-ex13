import os


def ping_ip(ip):
    result = os.popen(f"ping {ip}").read()
    return result
