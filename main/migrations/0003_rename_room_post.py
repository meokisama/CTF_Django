# Generated by Django 4.1.2 on 2022-11-02 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_room'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Room',
            new_name='Post',
        ),
    ]