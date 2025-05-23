# Generated by Django 5.1.4 on 2025-03-11 15:26

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Series', '0002_alter_serie_descripcion_alter_serie_generos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='plataformas',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('flow', 'Flow'), ('disney_plus', 'Disney Plus'), ('max', 'Max'), ('amazon_prime', 'Amazon Prime'), ('paramount', 'Paramount'), ('apple_tv', 'Apple TV'), ('netflix', 'Netflix'), ('Youtube TV', 'Youtube TV')], max_length=71, null=True),
        ),
    ]
