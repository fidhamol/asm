# Generated by Django 4.2.6 on 2023-10-25 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_projects_update'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]