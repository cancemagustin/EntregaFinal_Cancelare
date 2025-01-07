# Generated by Django 5.1.4 on 2025-01-03 22:21

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Series', '0004_alter_serie_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='genero',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('comedia', 'Comedia'), ('drama', 'Drama'), ('accion', 'Acción'), ('terror', 'Terror'), ('ciencia_ficcion', 'Ciencia Ficción'), ('romance', 'Romance'), ('documental', 'Documental'), ('fantasia', 'Fantasía'), ('misterio', 'Misterio'), ('aventura', 'Aventura')], max_length=89),
        ),
    ]
