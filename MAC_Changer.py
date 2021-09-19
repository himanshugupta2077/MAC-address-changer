#!/usr/bin/env python

import subprocess
import optparse

def get_arguements():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface" ,dest = "interface", help = "Interface to change it's MAC Address.")
	parser.add_option("-m", "--mac" ,dest = "new_mac", help = "New MAC Address for the interface.")
	(options, arguements) = parser.parse_args()
	
	if not options.interface:
		parser.error("[+]Please specify the interface, use --help or -h for more info.")
	if not options.new_mac:
		parser.error("[+]Please specify the new MAC Address, use --help or -h for more info.")
	return options
	
def change_mac(interface, new_mac):
	print(f"[+]Changing MAC Address of {interface} to {new_mac}")
	subprocess.run(["ifconfig", interface, "down"])
	subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.run(["ifconfig", interface, "up"])
	print(f"[+]Changed MAC Address of {interface} to {new_mac}")

options = get_arguements()
change_mac(options.interface, options.new_mac)
