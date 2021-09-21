# MAC Address Changer
MAC Address changer is a mini-project written in python to change the MAC address of the network interface in your hardware. 

It is compatible with 'Linux' machines only. 

## Features
- Only one line command to execute
- Error detection and help provided

## Tech
MAC Address changer uses a number of python modules to work properly:

- [subprocess] - To run linux & system commands from python code.
- [optparse] - To take user input in our code in a single line as an arguement.
- [re] - We use regex to search and store MAC Address of requested network interface into a string.

## Installation
MAC Address changer only requires python3.x and later version to run.

## Usage
Open terminal from the directory where code is saved and follow this syntax to run it:

```sh
python3 MAC_Changer.py -i [Network interface] -m [New MAC address]
```
and done!

##### For help: 
```sh
python3 MAC_Changer.py --help
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
