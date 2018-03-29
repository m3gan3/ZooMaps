# ZooMaps

# How to get started
1. Navigate to GTech folder.
2. Run the following commands:
  python manage.py makemigrations ZooMaps - This creates the database schema
  python manage.py migrate - This loads the migrations and populates the database with 25 users.
  python manage.py loaddata initial_data - This loads the superuser (compsci326) and some additional dummy data (Events, Tags, Users, etc.)
3. Run the following command:
  python manage.py runserver
4. Navigate to http://127.0.0.1:8000/
