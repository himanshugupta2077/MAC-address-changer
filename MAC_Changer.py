#!/usr/bin/env python

import subprocess

print('\nBelow is the list of Network Interfaces in your device with their properties listed below them: \n')

subprocess.call("ifconfig", shell=True)

interface = input("Enter Network Interface > ")
new_MAC = input(f"\nNew MAC address for {interface} > ")

print(f"Changing MAC Adress of {interface} to {new_MAC}")

subprocess.run(f"ifconfig {interface} down", shell=True)
subprocess.run(f"ifconfig {interface} hw ether {new_MAC}", shell=True)
subprocess.run(f"ifconfig {interface} up", shell=True)

check = input("\nTo check the MAC address press c:\nTo quit press q:\n")

if check == 'c':
	subprocess.call("ifconfig", shell=True)
elif check == 'q':
	exit()
