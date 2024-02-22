<p>
  <a href="https://exarth.com/">
  <img src="https://exarth.com/static/exarth/theme/logo-red-1000.svg" height="150">
  </a>
</p>
<hr>

# INTERN EASE 😕

_application tagline here_

Internease a web based application to facilitate students to get interships and organizations to get best internies.

# Applications

1. Website
2. Root Access
3. Administration
4. Student Portal
5. Organization Portal

# Tools and Technologies


| Category  | Tools and technologies                        |
| --------- | --------------------------------------------- |
| Frontend  | Html, Css, Javascript, JQuery, Ajax, Jinja    |
| Backend   | Django, Django-Rest-Framework``               |
| Databases | SQLite, PostGre                               |
| Server    | Linux based ubuntu server (aws/digital ocean) |

# Modules

1. [ ]  Authentication and Authorization
2. [ ]  Access and Permission Control System
3. [ ]  Notification Alerts and POP-ups
4. [ ]  Email Alerts
5. [ ]  Internship Management
6. [ ]  Organization Management
7. [ ]  Staff Management

----
# NEW TO PYTHON AND DJANGO
## Configurations
### Installations (step 1)
Make sure to install python first and then run the following commands.<br>
https://www.python.org/downloads/release/python-3100/

once installations are done make sure to check these commands on terminal or command prompt.<br>
```shell
python --version
pip --version
```
If you see the version of python and pip then you are good to go.

### Virtual Environment (step 2)
first install virtual environment using pip
```shell
pip install virtualenv
```
---

## How to run the project (First Time)
Unzip your project and navigate to the project folder and run the following commands <br>
(make sure you are in project directory) before running these commands.

### Step1 (create and activate virtual environment)
```shell
virtualenv venv
venv\Scripts\activate
```

### Step2 (install requirements and migrate database)
```shell
pip install -r requirements.txt
python manage.py makemigrations accounts company website
python manage.py migrate
```

## Step3 (run the server)
```shell
python manage.py runserver
```
----

## How to run the project later
(make sure you are in project directory) before running these commands.
```shell
venv\Scripts\activate
python manage.py runserver
```

# SUMMARY
<h4>ALERT !</h4>
<p>Application is developed by <a href="https://github.com/IkramKhan-DevOps/">MARK I</a> & <a href="https://github.com/Zarar-Anwar/">Zaala</a> at <b><a href="https://exarth.com">Exarth</a></b>.</p>