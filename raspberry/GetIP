#!/usr/bin/python
#获取本机ip

import os
import re

def valid_ip(ip):
    if ("255" in ip) or ( ip == "127.0.0.1") or ( ip == "0.0.0.0" ):
        return False
    else:
        return True

def get_ip(valid_ip):
    ipss = ''.join(os.popen("ifconfig").readlines())
    match = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    ips = re.findall(match, ipss, flags=re.M)
    ip = filter(valid_ip, ips)
    return ''.join(ip)

ip_addr = get_ip(valid_ip)
print(ip_addr)
