# Generated by Django 5.1 on 2024-08-15 03:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.TextField()),
                ('habilitado', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'categorias',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Golosinas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.TextField()),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(null=True, upload_to='imagenes')),
                ('habilitado', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(db_column='categoria_id', on_delete=django.db.models.deletion.PROTECT, to='gestion.categoria')),
            ],
            options={
                'db_table': 'golosinas',
                'ordering': ['nombre', 'precio'],
                'unique_together': {('nombre', 'precio')},
            },
        ),
    ]
