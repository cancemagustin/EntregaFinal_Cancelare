# Generated by Django 5.1.4 on 2025-01-20 14:05

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Series', '0011_alter_serieguardada_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='genero',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('comedia', 'Comedia'), ('drama', 'Drama'), ('accion', 'Acción'), ('terror', 'Terror'), ('ciencia_ficcion', 'Ciencia Ficción'), ('romance', 'Romance'), ('documental', 'Documental'), ('Fantasía', 'Fantasía'), ('misterio', 'Misterio'), ('aventura', 'Aventura'), ('política', 'Política')], max_length=98),
        ),
    ]
