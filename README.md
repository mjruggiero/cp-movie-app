# Clever Movie Full Stack App
This is a movie app using Django.
This is a project from the [Clever Programmer](https://clever-programmer.com) Profit with Python course.

## Contents

1. [Initial Setup Instructions](#initial-setup-instructions)
1. [Running Server](#running-server)


## Initial Setup Instructions

### Setup Python Virtual Environment
```buildoutcfg
# Create the virtual environment
$ python3 -m venv venv

# Activate the virtual environment
. venv/bin/activate

# Install the dependencies
pip3 install -r requirements.txt
```
## Running Server

```buildoutcfg
./mange.py migrate
./mange.py runserver
```
### Open a web browser and load the URL `http://127.0.0.1:8000/`