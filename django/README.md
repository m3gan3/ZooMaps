# ZooMaps

## Setup

1. Navigate to <https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment> for directions on how to install and run Django and virtualenv.

2. Clone this repository.

3. Once set up, run `pip install -r requirements.txt` to download the required dependencies for this project. Included are development related dependencies, such as 'hypothesis' and 'flake8'.

## Running the project
(RECOMMENDED) This repository includes a pre-loaded 'db.sqlite3' database file and can thus be run as is using the following:

1. Navigate to the 'GTech/GTech/' folder.
2. Run the following command:
  python manage.py runserver
3. Navigate to http://127.0.0.1:8000/

 To clear the database and remake the database schema and migrations, either delete the 'ZooMaps/migrations' folder and 'db.sqlite3' file, or run './run.py clean' in the command line. Then, to remake the migrations, use either 'python manage.py makemigrations' and 'python manage.py migrate' in succession, or './run.py build'. As of 4-30-2018, we cannot guarantee that the project can be rebuilt this way. Scripts to programmatically populate the database are a feature that needs to be implemented.

 ## Extras
 Included in the project is a 'run.py' development script. Its purpose is to perform tasks related to development, including, but not limited to: running the server, making database migrations, cleaning the project of migrations files, and linting the project code. It currently takes '', 'runserver', 'build', 'clean', and 'lint' as arguments.


