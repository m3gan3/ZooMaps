# Generated by Django 2.0.2 on 2018-03-09 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ZooMaps', '0007_auto_20180309_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField(help_text='Enter a brief comment for the event', max_length=1000)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ZooMaps.Event')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ZooMaps.User')),
            ],
        ),
    ]