#!/usr/bin/env python

import subprocess

print('Below is the list of Network Interfaces in your device with their properties listed below them: \n')

subprocess.call("ifconfig", shell=True)

interface = input("Enter the network interface you want to change name of: ")
new_MAC = input("Enter new MAC address for the selected inteface: ")

subprocess.run(f"ifconfig {interface} down", shell=True)
subprocess.run(f"ifconfig {interface} hw ether {new_MAC}", shell=True)
subprocess.run(f"ifconfig {interface} up", shell=True)

