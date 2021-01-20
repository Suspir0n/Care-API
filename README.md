#  Care - API Rest in python flask

## Description
This project illustrates an api in python and Flask.

## Starting

To run the project, you will need to install the following programs:

- [Python: Required to create the project](https://www.python.org/downloads/)
- [Mysql: Required a database to create the tables etc](https://www.mysql.com/)
- [VS Code: For project development](https://code.visualstudio.com/)

## ⌨️ Development

Use Gitpod, a free online dev environment for GitHub.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Suspir0n/Care-API.git)

Or use code locally using:
```
$ cd "directory of your choice"
$ git clone https://github.com/Suspir0n/Care-API.git
```

### Construction

To build the api with Flask, execute the commands below:

```
$ pip3 install -r requirements.txt
```

These are the requirements.txt dependencies:

```
Flask==1.1.2
flask-marshmallow==0.14.0
Flask-SQLAlchemy==2.4.4
marshmallow==3.9.1
marshmallow-sqlalchemy==0.24.0
PyJWT==1.7.1
PyMySQL==0.10.1
pyparsing==2.4.7
pytest==6.1.2
SQLAlchemy==1.3.20
pytest-flask
pytest-cov
```

To run the program in flask first add the main file in FLASK_APP

In Windows
```
$ set FLASK_APP=yourfile.py
$ flask run
```

In Mac
```
$ export FLASK_APP=yourfile.py
$ flask run
```

The exit:

```
* Serving Flask app "yourfile.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

If you want to choose the host where it runs run this command

```
$ flask host 0.0.0.0
```

## Features

The project can be used as a model to start the development of a Python project using Flask. It also demonstrates in a practical way how to create a Flask api quickly and easily.

## Configuration

To execute the project, it is necessary to use VsCode or an IDE of your preference, so that it identifies the dependencies necessary for execution in the repository. Once the project is imported, it will be possible to test its functionality in real time.

## Contributions

Contributions are always welcome! I hope I have helped someone in need.

