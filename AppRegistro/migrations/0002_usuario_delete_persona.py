# Generated by Django 4.0.3 on 2022-04-06 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRegistro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('id_usuario', models.CharField(max_length=50, verbose_name='apellido')),
                ('contraseña', models.CharField(max_length=50, verbose_name='contraseña')),
            ],
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
    ]