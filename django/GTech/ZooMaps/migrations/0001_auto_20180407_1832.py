# Generated by Django 2.0.2 on 2018-04-07 22:32

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ZooMaps', 'initial_populate_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(-1)])),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='Enter your username', max_length=20)),
                ('password', models.CharField(default='', help_text='Enter your password', max_length=20)),
                ('emailAddress', models.CharField(default='', help_text='Enter your email address', max_length=20)),
                ('first_name', models.CharField(help_text='Enter your first name', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='commentevent',
            name='event',
        ),
        migrations.RemoveField(
            model_name='commentevent',
            name='username',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='latitue',
            new_name='latitude',
        ),
        migrations.RemoveField(
            model_name='messageevent',
            name='object',
        ),
        migrations.AddField(
            model_name='messageevent',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(help_text='Users going to your Event', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='messageevent',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CommentEvent',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='ratingevent',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ZooMaps.Event'),
        ),
        migrations.AddField(
            model_name='ratingevent',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
