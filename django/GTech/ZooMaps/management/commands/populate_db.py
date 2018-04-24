from django.core.management.base import BaseCommand, CommandError
from django.db import migrations
from django.apps import apps
import ZooMaps.models
import random

def make_users(apps, schema_editor):
    '''
    Creates a set of 25 users for the database

    BUG: Currently not working due to changes in models.
    Current version based on previous version of models.py
    Creates users with garbage values...
    '''
    EMAIL_DOMAINS = ['umass.edu',
                    'icloud.com',
                    'gmail.com',
                    'yahoo.com',
                    'protonmail.com',
                    'lavabit.com',
                    'aol.com'
                    ]
    UserModel = apps.get_model('ZooMaps', 'UserModel')
    print(UserModel._meta.fields)
    for i in range(1, 26):
        username = '{:0>3}'.format(str(i))
        password = username
        domain = random.choice(EMAIL_DOMAINS)
        email_address = f'{username}@{domain}'
        first_name = '{:0>3}'.format(i)
        UserModel.objects.get_or_create(username=username, password=password, emailAddress=email_address, first_name=first_name)


class Command(BaseCommand):
    help = 'Populates database with mock data using models'

    def handle(self, *args, **options):
        app = apps.get_app_config('ZooMaps')
        migrations.RunPython(make_users)

