# Generated by Django 3.2.4 on 2021-07-12 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitioVet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='nombre',
            new_name='nombreAnimal',
        ),
    ]
