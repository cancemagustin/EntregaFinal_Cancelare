# Generated by Django 5.1.4 on 2025-02-10 14:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Series', '0017_opinion_serie_estrellas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion_serie',
            name='estrellas',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
