# Generated by Django 2.0.2 on 2018-03-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZooMaps', '0003_auto_20180309_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='endDate',
            field=models.DateTimeField(blank=True, default='2018-06-16', null=True),
        ),
    ]