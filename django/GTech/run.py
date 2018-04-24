#!/usr/bin/env python3
import os, sys, subprocess, argparse
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command
from distutils.util import strtobool

"""
Master script that takes optional arguments and runs the correspoding script.
The script's purpose is to perform common tasks such as running the server,
making migrations, running tests, etc. Runs the server by default if no argument
is provided.

Where Django provides admin/mangage.py methods, the 'call_command' method is used.
Otherwise, terminal-based commands are executed using the 'os' module's 'system' method.

Note: This script assumes a UNIX-like environment.

TODO: Consider refactoring this into two scripts, 'run.py' and 'dev.py', if
it becomes too flooded with functionality.
"""

def print_cmd(cmd):
    '''
    Method to print the shell command and arguments to stdout.

    Args:
        cmd (str): String representing command to be run
    Returns:
        None
    '''
    print('Running: {0}\n'.format(' '.join(a for a in [cmd])))
    sys.stdout.flush()  # Make sure stdout is flushed before continuing.


def is_database_synchronized(database):
    '''
    Method to check if migrations need to be made.
    TODO: Explain more. AFAIK, it checks that the leaves of the existing migration graph
    are the same as those that would be added should migrations be made.
    '''
    connection = connections[database]
    connection.prepare_database()
    executor = MigrationExecutor(connection)
    targets = executor.loader.graph.leaf_nodes()
    if executor.migration_plan(targets):
        return False
    else:
        return True


def apply_migrations():
    print('Creating/updating database...')

    print_cmd('python manage.py makemigrations ZooMaps')
    call_command('makemigrations', 'ZooMaps')

    print_cmd('python manage.py migrate')
    call_command('migrate')


def prompt_user(prompt):
    '''
    Recursively repeats a prompt until the user enters in a 'yes' or 'no' value.
    'True' and 'False' values are 'y' and 'yes' and 'n' and 'no', respectively.

    Returns: The value 'True' if the user enters in an affirmative value.
    'False' if the user enters in a 'falsey' value.
    '''
    YES_VALS = ['y', 'yes']
    NO_VALS = ['n', 'no']

    yes_or_no = str(input(prompt)).lower().strip()
    if yes_or_no in YES_VALS:
        return True
    elif yes_or_no in NO_VALS:
        return False
    else:
        return prompt_user(prompt)


if __name__ == '__main__':

    proj_path = os.getcwd()
    # This is so Django knows where to find stuff.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GTech.settings")
    sys.path.append(proj_path)

    # This is so my local_settings.py gets loaded.
    os.chdir(proj_path)

    # Specify relative directories for which to lint and run tests from
    LINT_DIRS = [
        'ZooMaps/',
        'tests/',
    ]

    TEST_DIRS = [
        'tests/'
    ]

    # This is so models get loaded.
    application = get_wsgi_application()

    # Import modules to allow for checking of database migrations
    from django.db.migrations.executor import MigrationExecutor
    from django.db import connections, DEFAULT_DB_ALIAS

    # Get the given command line argument, if there is one, representing the actions to perform.
    args = sys.argv[1:]
    cmd = None
    if args:
        cmd = args[0]

    # Run server if no argument provided
    if not cmd or cmd == 'server':
        # TODO check if migrations need to be performed, if they do, prompt user to perform them.
        if is_database_synchronized(DEFAULT_DB_ALIAS):
            # All migrations applied. Proceed with running server.
            # Chose not to print the explicit command w/ print_cmd() because Django will reload, thus printing it 2+ times.
            call_command('runserver',  '127.0.0.1:8000')
        else:
            # Unapplied migrations. Prompt user to run them. Then run the server

            apply_migrations = prompt_user('Unapplied migrations detected. Would you like to apply them (Y/N)?')
            if not apply_migrations:
                print('Migrations will not be applied. Exiting')
            else:
                apply_migrations()
                print('Migrations made. Running server')
                call_command('runserver',  '127.0.0.1:8000')
    elif cmd == 'build':
        apply_migrations()
    elif cmd == 'test':
        # Runs all test files starting with '*test' in /tests directory relative to path this script is in.
        print('Running test suite in tests directory')
        cmd_to_run = 'python manage.py test {}'.format(' '.join(TEST_DIRS))
        print_cmd(cmd_to_run)
        call_command('test', 'tests/')
    elif cmd == 'lint':
    # Runs a linter over the code in the paths specified by LINT_PATHS.
    # Will check for Flake8
        LINT_SETTINGS = ['--format', '%(path)s [%(row)s:%(col)s] %(code)s: %(text)s',
                        '--show-source']
        cmd_to_run = 'flake8' + ' '.join(LINT_DIRS) + ' '.join(LINT_SETTINGS)
        print_cmd(cmd_to_run)

        try:
            from flake8.main.application import Application as Flake8
        except ImportError as e:
            print('Cannot load module: {0!r}'.format(e))
        else:
            linter = Flake8()
            linter.run(LINT_DIRS + LINT_SETTINGS)
    elif cmd == 'clean':
        # Clean extraneous files like '__init__.py' files, pycache directories, migrations files generated by Django, etc.
        want_clean = prompt_user('You are about to delete migrations files. Would you like to proceed (Y/N)?')
        if not want_clean:
            print('Files will not be deleted. Exiting.')
        else:
            print('Deleting files...')
            cmd_to_run = 'find . -path "*/migrations/*.py" -not -name "__init__.py" -delete'
            print_cmd(cmd_to_run)
            os.system(cmd_to_run)

            cmd_to_run = 'find . -path "*/migrations/*.pyc" -delete'
            print_cmd(cmd_to_run)
            os.system(cmd_to_run)
    sys.exit()
