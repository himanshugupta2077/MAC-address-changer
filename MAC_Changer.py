#!/usr/bin/env python

import subprocess

print('\n\nBelow is the list of Network Interfaces in your device with their properties listed below them: \n')

subprocess.call("ifconfig", shell=True)

interface = input("Enter the network interface you want to change name of: ")
new_MAC = input("\nEnter new MAC address for the selected inteface: ")

subprocess.run(f"ifconfig {interface} down", shell=True)
subprocess.run(f"ifconfig {interface} hw ether {new_MAC}", shell=True)
subprocess.run(f"ifconfig {interface} up", shell=True)

check = input("To check the MAC address of the desired interface press c and to quit press q: ")

if check == c:
	subprocess.call("ifconfig", shell=True)
else:
	break

