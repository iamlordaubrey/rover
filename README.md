# Rover Control

Description: An Rover Control application that either takes in input from the command line or reads input
from file and moves the rover based on input

### Assumptions
- Each rover always has both landing and instructions input
  - A rover with only one of these (landing but no instructions or instructions but no landing) would be discarded
- Rovers instructions don't permit rover to move beyond the plateau boundary. Adding this to v2.0 :)

### Tech Stack
Built using Python 3.10.5 (see `.python-version` file). Libraries are kept as minimal as possible 
(see `requirements.in` file)


## Install
Creates a fresh virtual environment (called .venv) and installs requirements
```commandline
make setup
```

## Run
Run a single instance of the wsgi server for local development

Install pip requirements
```commandline
make pip_sync
```

### Run rover control
#### via command line, run:
```commandline
python main.py
```
#### via file, run:
```commandline
python main.py sentry 
```
Alternatively, import the function `sentry` and call the sentry function directly,
passing no arguments. The function gets its input from file.

Run tests
```commandline
make runtest
```
