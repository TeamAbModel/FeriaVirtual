# Generated by Django 3.0.7 on 2020-06-07 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feria',
            fields=[
                ('feria_id', models.CharField(help_text='Ingrese ID de la Feria', max_length=10, primary_key=True, serialize=False)),
                ('feria_calle', models.CharField(help_text='Ingrese Nombre de la Calle de la Feria', max_length=200)),
                ('feria_comuna', models.CharField(help_text='Ingrese el Comuna de la feria', max_length=200)),
                ('feria_direccion_ini', models.CharField(help_text='Ingrese la Direccion Inicial de la feria', max_length=200)),
                ('feria_direccion_fin', models.CharField(help_text='Ingrese la Direccion Final de la feria', max_length=200)),
                ('feria_horario_ini', models.CharField(help_text='Ingrese la Horario Inicial de la feria', max_length=200)),
                ('feria_horario_fin', models.CharField(help_text='Ingrese la Horario Final de la feria', max_length=200)),
                ('feria_dias', models.CharField(help_text='Ingrese dias de la feria', max_length=200)),
                ('feria_imagen', models.ImageField(null=True, upload_to='gallery')),
            ],
        ),
    ]
