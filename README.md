# Bank security console

This script is a security console.
It contains information about employees
located in the vault, having access cards,
and also gives detailed information about visits
storage for each employee.

## How to install

Python3 should already be installed. Then use pip
(or pip3 if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
``` 

### will be installed:

django==3.2.19
psycopg2-binary==2.9.6
environs~=9.5.0
python-dotenv==1.0.0

## Environment variables

You need to create a **.env** file, it should contain:

```bash
SECRET_KEY=''
PASSWORD_BD=''
HOST_BD=''
PORT_BD=''
NAME_BD=''
USER_BD=''
DEBUG='False'
```

## How to use

To run the program python manage.py runserver 0.0.0.0:8000.

```bash
$ python manage.py runserver 0.0.0.0:8000
Performing system checks...

System check identified no issues (0 silenced).
August 18, 2023 - 15:55:50
Django version 3.2.19, using settings 'project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CTRL-BREAK.

```

## Project Goals

The code is written for educational purposes on online-course for web-developers dvmn.org.
