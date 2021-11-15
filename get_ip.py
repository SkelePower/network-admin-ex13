import os


def get_local_ip():
    ipconfig_result = os.popen("ipconfig").read()
    ipconfig_list = ipconfig_result.split("\n\n")
    for segment_index in range(len(ipconfig_list)):
        if "Ethernet adapter Ethernet:" in ipconfig_list[segment_index]:
            inner_list = ipconfig_list[segment_index + 1].split("\n")
            for line in inner_list:
                if "IPv4 Address" in line:
                    return line[39:]


def get_subnet_mask():
    ipconfig_result = os.popen("ipconfig").read()
    ipconfig_list = ipconfig_result.split("\n\n")
    for segment_index in range(len(ipconfig_list)):
        if "Ethernet adapter Ethernet:" in ipconfig_list[segment_index]:
            inner_list = ipconfig_list[segment_index + 1].split("\n")
            for line in inner_list:
                if "Subnet Mask" in line:
                    return line[39:]


def get_public_ip():
    result = os.popen("nslookup myip.opendns.com resolver1.opendns.com").read()
    result_list = result.split("\n")
    first_address = False
    for line in result_list:
        if "Address" in line:
            if first_address:
                return line[10:]
            else:
                first_address = True
