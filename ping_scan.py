import os
import threading
from netaddr import IPNetwork, IPAddress


def is_up(ip, up):
    result = os.popen(f"ping {ip} -n 1").read()
    if "Destination host unreachable" not in result and\
            "Request timed out" not in result:
        up.append(ip)


def ping_scan(ip, subnet_mask):
    up = []
    subnet_mask_slash = IPAddress(subnet_mask).netmask_bits()
    ip_list = IPNetwork(f"{ip}/{subnet_mask_slash}")
    th = []
    for ip in ip_list:
        th.append(threading.Thread(target=is_up, args=(str(ip), up)))
        th[-1].start()
    for t in th:
        t.join()
    return up
