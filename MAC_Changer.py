#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguements():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface" ,dest ="interface", help = "Interface to change it's MAC Address.")
	parser.add_option("-m", "--mac" ,dest = "new_mac", help = "New MAC Address for the interface.")
	(options, arguements) = parser.parse_args()

	if not options.interface:
		parser.error("[-]Please specify the interface, use --help or -h for more info.")
	if not options.new_mac:
		parser.error("[-]Please specify the new MAC Address, use --help or -h for more info.")
	return options

def change_mac(interface, new_mac):
	print(f"[+]Changing MAC Address of {interface} from {current_mac} to {new_mac}")
	subprocess.run(["ifconfig", interface, "down"])
	subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.run(["ifconfig", interface, "up"])

def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig", interface])
	ifconfig_result = ifconfig_result.decode('utf-8')

	re_searched_mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
	re_searched_mac_address = re_searched_mac_address.group(0)
	print(f"[+]Current MAC Address --> {re_searched_mac_address}")
	return re_searched_mac_address

def final_check():
	if current_mac == options.new_mac:
		print(f"[+]Successfully changed MAC Address of {options.interface} to {current_mac}")
	else:
		print("[-]Could not change MAC address, use --help or -h for more info.")

options = get_arguements()

current_mac = get_current_mac(options.interface)

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)

final_check()
