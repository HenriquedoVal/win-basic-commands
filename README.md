# win-basic-tools

Description:
This repository intends to give some simple commands to Windows cmd.exe and Powershell(not yet) for better interoperability to WSL users.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stablw/) to install win-basic-tools

~~~bash
pip install win-basic-tools
~~~

## Usage

Run setup_cmd.py for setting the macros file for your cmd.exe. It will create the .macros.doskey at your home directory and add it to the Registry.
This will create the alias to the /source/ resources and to some of the CLI commands present on Windows as the most commom Unix commands. Especially useful for WSL users that need an single command syntax between systems.
See setup_cmd.py for the list of aliases.

## License

[MIT](https://choosealicense.com/licenses/mit/)
