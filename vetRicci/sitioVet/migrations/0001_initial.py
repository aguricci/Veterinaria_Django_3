# Generated by Django 3.2.4 on 2021-07-12 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('idAnimal', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Animal')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de Animal')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('idMascota', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Mascota')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre de Mascota')),
                ('telefonoDuenio', models.CharField(max_length=15, verbose_name='Telefono del Dueño')),
                ('idAnimal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitioVet.animal')),
            ],
        ),
    ]
