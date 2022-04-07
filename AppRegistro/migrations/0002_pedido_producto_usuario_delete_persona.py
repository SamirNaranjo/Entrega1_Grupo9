# Generated by Django 4.0.3 on 2022-04-06 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRegistro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_pedido', models.IntegerField(verbose_name='Numero de Pedido')),
                ('fecha_pedido', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=30, verbose_name='Nombre del Producto')),
                ('cantidad_producto', models.IntegerField(verbose_name='Cantidad de Producto')),
                ('precio_producto', models.FloatField(verbose_name='Precio del producto')),
            ],
        ),
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