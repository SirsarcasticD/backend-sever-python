# Project

Requires Python 3.7

## Installation
* Clone the repository. `git clone https://github.com/SirsarcasticD/backend-sever-python.git`
* Update the system. `sudo apt-get update`
* Install python. `sudo apt install python3-pip -y`
* Create a new virtualenv `python3 -m venv venv`.
* Source into your newly created virtualenv `source venv/bin/activate`.
* Install the requirements by running: `./dependencies.sh`.

## Setup Complete
* Start the server: `./manage.py runserver 0.0.0.0:8000`.
* Test the server is running on your local machine: `curl --location --request GET 'http://127.0.0.1:8000/ping/'`
* You should receive a response of: `{"ping": "ok"}`

## Database Configuration
* Create and host a postgresql (or other) database.
* Configure the `alembic.ini` (line 42) and `webapp/models/base.py` (line 16) files by adding the path to your database in the form of `database_type://username:password@IP:Port/path_to_database/database_name`. 
* Build the database schema by running: `alembic upgrade head`.
* Populate the database with required data `./populate_database.sh`.

## Development
* Create a feature branch off of the dev branch.
* Ensure your database schema are up-to-date by running: `alembic upgrade head`.
* Add required tests.
* Start the server: `./manage.py`.
* Run the test suite: `python -m unittest`.
* Check if you have any linting errors by running: `lint`.
* If everything is good, push your branch to github.
* Go on github and create a pull request to merge your feature branch into dev.
* CircleCI will build and test your branch.
* The maintainer will be able to review the code.
* The maintainer will accept the pull request.
* This will trigger a dev build **and deployment**.

## Deployments
**ALL DEPLOYMENTS MUST BE DONE THROUGH THE PULL REQUEST SYSTEM.**
