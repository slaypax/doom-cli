# Doom-Cli #

Doom-Cli is a command line interface wrapped around the fantastic [RESTful-Doom project.](https://github.com/jeff-1amstudios/restful-doom)

# Build #

Install the tool in virtualenv

`code()`
 $ git clone github.com/slaypax/doom-cli.git
 $ python3 -m venv doom-cli
 $ cd doom-cli
 $ pip install .

# Run #

Make sure you install and configure RESTful-doom. This tool needs a running RESTful-doom server to interact with. Current implmentation assumes the server is running on the default host/port. Type doom --help for details on usage and avaiable commands. 
