# Generated by Django 3.2.7 on 2023-09-29 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_contactform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='title',
            new_name='full_name',
        ),
    ]
