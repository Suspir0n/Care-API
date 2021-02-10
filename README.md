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
flask==1.1.2
pytest==6.1.2
flask-sqlalchemy==2.4.4
pymysql==1.0.2
flask-marshmallow==0.14.0
PyJWT==2.0.1
PyTest
```

Make these settings so that your Flask application works perfectly

In Windows
```
$ set FLASK_APP=yourfile.py
$ set FLASK_ENV=Development
$ set FLASK_DEBUG=True
```

In Mac
```
$ export FLASK_APP=yourfile.py
$ export FLASK_ENV=Development
$ export FLASK_DEBUG=True
```

#### Database configuration 

I will show you how to connect to the mySQL database 
and its configuration. Remember, it does not create the 
database alone or the table so you have to create the 
database and tables first.

```
def connect_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/yourdatabase'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
def config_db(app):
    db.init_app(app)
    app.app_context().push()
    db.create_all(app=app)
    app.db = db
```

After you set up the database, run your flask application
```
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

After running the application, a link will appear where it is 
being executed, accessing it you should see this page, use Postman
to have a better visibility

<img src="./prototitypes/prototitype-001.png">

With that we will have to do the authentication so that you can 
use the other routes<br><br>

We will have to pass a json, in the case to register / post so 
that we can authenticate

```
{
    "first_name": "Admin",
    "last_name": "Teste",
    "email": "teste@gmail.com",
    "password": "admin"
}
```
The login will be the data you will pass on "first_name"

<img src="./prototitypes/prototitype-002.png">

## Token Authenticate with JWT

With the admin user created, we can authenticate by sending 
a POST request with authentication of the "BASIC" format to 
the IP: http://127.0.0.1:5000/auth, filling in the "USERNAME" 
and "PASSWORD", as below:<br><br>
<img src="./prototitypes/prototitype-003.png">


## Unit Test
The unit tests of routes were created using pytest, just run the command:

```
$ pytest tests\ -v -s
```
<img src="./prototitypes/prototitype-004.png">

## Project Structure

```
|-- app
   |-- controllers
      |-- __init__.py
      |-- address_controller.py
      |-- base_controller.py
      |-- card_controller.py
      |-- cart_controller.py
      |-- category_controller.py
      |-- helpers.py
      |-- new_product_controller.py
      |-- sub_category_controller.py
      |-- user_controller.py
   |-- models
      |-- __init__.py
      |-- address_model.py
      |-- card_model.py
      |-- cart_model.py
      |-- category_model.py
      |-- new_product_model.py
      |-- sub_category_model.py
      |-- user_model.py
   |-- routes
      |-- __init__.py
      |-- address_routes.py
      |-- card_routes.py
      |-- cart_routes.py
      |-- category_routes.py
      |-- new_product_routes.py
      |-- sub_category_routes.py
      |-- user_routes.py
   |-- schemas
      |-- __init__.py
      |-- address_serealize.py
      |-- card_serealize.py
      |-- cart_serealize.py
      |-- category_serealize.py
      |-- new_product_serealize.py
      |-- sub_category_serealize.py
      |-- user_serealize.py
   |-- settings
      |-- __init__.py
      |-- config.py
      |-- connection.py
   |-- __init__.py
|-- prototitypes
   |-- prototitype-001.png
   |-- prototitype-002.png
   |-- prototitype-003.png
   |-- prototitype-004.png
|-- tests
   |-- happy_way
      |-- test_field_validation
         |-- __init__.py
         |-- field_validation_user_test.py
      |-- test_routes
         |-- routes_address_test.py
         |-- routes_card_test.py
         |-- routes_cart_test.py
         |-- routes_category_test.py
         |-- routes_product_test.py
         |-- routes_sub_category_test.py
         |-- routes_users_test.py
      |-- __init__.py
   |-- sad_way
      |-- __init__.py
   |-- __init__.py
   |-- app_test.py
   |-- conftest.py
|-- venv
|-- .gitignore
|-- __init__.py
|-- README.md    
|-- requirements.txt
```
app >> folder contains all API data, controlles, models, schemas, 
settings, all necessary data.
<br><br>
test folder >> contains route tests and field validation on the 
sad and happy path.
<br><br>
venv >> folder contains all the data of the premises that you 
will use.
<br><br>

## Features

The project can be used as a model to start the development of a Python project using Flask. It also demonstrates in a practical way how to create a Flask api quickly and easily.

## Configuration

To execute the project, it is necessary to use VsCode or an IDE of your preference, so that it identifies the dependencies necessary for execution in the repository. Once the project is imported, it will be possible to test its functionality in real time.

## Contributions

Contributions are always welcome! I hope I have helped someone in need.

## Credits

I want to thank Matheus Miller because he was able to learn how to
create a part of the API itself.<br><br>
His repository: https://github.com/MatheusMullerGit/api-rest-flask-jwt-authentication
<br>
Linkedin: https://www.linkedin.com/in/matheus-herrera-bezerra-muller/

## 🔓 License
MIT © [Evandro Silva](https://www.linkedin.com/in/suspir0n/)