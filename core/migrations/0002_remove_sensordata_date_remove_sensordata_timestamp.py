# Generated by Django 4.2.2 on 2024-08-09 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensordata',
            name='date',
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='timestamp',
        ),
    ]
