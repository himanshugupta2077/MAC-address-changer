# MAC Address Changer
## _Stay annonymous_

MAC Address changer is a mini-project written in python to change the MAC address of the network interface in your hardware. 

It is compatible with 'Linux' machines only. 

## Features
- Requires python3.x only
- Only one line command to execute
- Error detection and help provided

## Tech

MAC Address changer uses a number of python modules to work properly:

- [subprocess] - To run linux & system commands from python code.
- [optparse] - To take user input in our code in a single line as an arguement.
- [re] - We use regex to search and store MAC Address of requested network interface into a string.

And of course this tool itself is open source with a [public repository] on GitHub.

## Installation

MAC Address changer only requires python3.x to run.

Open terminal from the directory where code is saved and follow this syntax to run it:

```sh
python3 MAC_Changer.py -i [Network interface] -m [New MAC address]
```
and done!

### For more help: 
```sh
python3 MAC_Changer.py --help
```

## License

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
