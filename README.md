# MAC Address Changer
MAC Address changer is a mini-project written in python to change the MAC address of the network interface in your hardware. 

Compatible with Linux machines

## Tech
Python Libraries Used:

- [subprocess] - To run linux & system commands from python code.
- [optparse] - To take user input in our code in a single line as an arguement.
- [re] - We use regex to search and store MAC Address of requested network interface into a string.

## Installation
MAC Address changer only requires python3.x and later version to run.

## Usage

```sh
python3 MAC_Changer.py -i [Network interface] -m [New MAC address]
```

##### For help: 
```sh
python3 MAC_Changer.py --help
```
