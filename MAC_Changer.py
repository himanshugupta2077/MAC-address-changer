#!/usr/bin/env python

#Subprocess can execute linux as well as all system commands.
#It contains no. of functions which allow us to execute system commands(respective to OS).
import subprocess

#Outparse allows us to take user input in our code as arguement and use it.[Command line arguements]
import optparse

#initializing a variable(object) parser which uses(inherits) properties of OptionParser class.
parser = optparse.OptionParser()

#adding options to parser using module 'add_option'
parser.add_option("-i", "--interface" ,dest = "interface", help = "Interface to change it's MAC Address.")

parser.add_option("-m", "--mac" ,dest = "new_MAC", help = "New MAC Address for the interface.")

#returns to set of information: I is options, II is args. We use 2 new variables to store them in order.
(options, arguements) = parser.parse_args()

#print('\n--> List of Network Interfaces: \n')
#subprocess.call("ifconfig", shell=True)

interface = options.interface
new_MAC = options.new_MAC

print(f"[+]Changing MAC Address of {interface} to {new_MAC}")

subprocess.run(["ifconfig", interface, "down"])
subprocess.run(["ifconfig", interface, "hw", "ether", new_MAC])
subprocess.run(["ifconfig", interface, "up"])

print(f"[+]Changed MAC Address of {interface} to {new_MAC}")
