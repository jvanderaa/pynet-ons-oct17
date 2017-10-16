#!/usr/bin/env python
from __future__ import print_function, unicode_literals
from getpass import getpass
from netmiko import ConnectHandler

if __name__ == "__main__":

    password = getpass("Enter password: ")
    cisco1 = {
        'device_type': 'cisco_ios',
        'ip':   '184.105.247.70',
        'username': 'pyclass',
        'password': password
    }

    net_connect = ConnectHandler(**cisco1)
    print(net_connect.find_prompt())
