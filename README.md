# Setting up the CRUD REST API
Single Resource CRUD REST API. 

This project uses Django 3.2 LTS and been written with Python 3.9.
We use Pipenv for package management and virtualization.

# Installation
## Install Pipenv
We use pipenv to manage our Python packages and virtualenv all in one.

```shell
% pip install pipenv
```

## Install Django Framework and Dependencies using Pipenv
Install Django Framework, dependencies, and dev packages

We use [HTTPIE](https://httpie.io/) over curl commands to run CRUD operations from the CLI. Promise it's much better!

```shell
% pipenv install --dev
```

Enter into the Virtualenv and check that the packages have installed correctly. 
Below is an example of the packages that installed

```shell
% pipenv shell 
% pip list

Package             Version
------------------- ---------
asgiref             3.4.1
attrs               21.2.0
certifi             2021.10.8
charset-normalizer  2.0.7
defusedxml          0.7.1
Django              3.2.9
django-filter       21.1
djangorestframework 3.12.4
drf-spectacular     0.20.2
httpie              2.6.0
idna                3.3
inflection          0.5.1
jsonschema          4.2.1
pip                 21.2.4
Pygments            2.10.0
pyrsistent          0.18.0
PySocks             1.7.1
pytz                2021.3
PyYAML              6.0
requests            2.26.0
requests-toolbelt   0.9.1
setuptools          58.1.0
sqlparse            0.4.2
uritemplate         4.1.1
urllib3             1.26.7
wheel               0.37.0
```

Now that we have all the packages installed, let's run the server

# Running the Application

To run the API Server, make sure you are in the venv.

```shell
% pipenv shell
% cd widget_project
% python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 08, 2021 - 02:38:05
Django version 3.2.9, using settings 'widget_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

# Accessing the API EndPoints

The following endpoints have been exposed:

    * /widgets/             # List View
    * /widgets/:id>/        # Detailed View via the id

## Accessing Endpoints from the CLI

Use `http` to access the endpoints. Some examples are provided below:


```shell
% http GET http://localhost:8000/widgets/
% http PUT http://localhost:8000/widgets/1/ name="Weather" parts=3
% http DELETE http://localhost:8000/widgets/3/
```
## Accessing Endpoints from the Browser

Thanks to Django Framework a browsable API is available for the Widget

`List View`

http://localhost:8000/widgets/

`Detailed View`

http://localhost:8000/widgets/1/
# OpenAPI Spec

Once the server is running, you can check out the OpenAPI spec by visiting:

http://localhost:8000/docs

# Testing

There currently exists 1 Unit Test for the model itself and 4 Functional Tests for each CRUD operation. 

## Locate the tests in the Repository 
Tests can be located in `widget_project->widget->test.py`

## Running the tests

```shell
% pipenv shell
% cd widget_project
% python manage.py test
```

